const puppeteer = require('puppeteer');
const { Configuration, OpenAIApi } = require('openai');
require('dotenv').config();

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

async function scrapeAndAnswer() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Go to a sample page with questions
  await page.goto('https://example.com/faq');

  // Grab some questions from the page
  const questions = await page.$$eval('.question', els => els.map(el => el.textContent.trim()));

  for (const question of questions) {
    const response = await openai.createChatCompletion({
      model: "gpt-4",
      messages: [{ role: "user", content: question }],
    });

    console.log(`Q: ${question}`);
    console.log(`A: ${response.data.choices[0].message.content}\n`);
  }

  await browser.close();
}

scrapeAndAnswer();
