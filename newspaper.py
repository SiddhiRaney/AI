from newspaper import Article
import pandas as pd

# Function to extract article info
def extract_article_info(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        
        return {
            "URL": url,
            "Title": article.title,
            "Authors": article.authors,
            "Published Date": article.publish_date,
            "Summary": article.summary,
            "Text": article.text[:500]  # first 500 chars
        }
    except Exception as e:
        return {
            "URL": url,
            "Error": str(e)
        }

# List of news URLs
urls = [
    "https://www.bbc.com/news/world-us-canada-68870145",
    "https://www.nytimes.com/2024/04/05/world/europe/france-retirement-age.html",
    "https://edition.cnn.com/2023/11/03/tech/twitter-x-advertising/index.html",
    "https://www.aljazeera.com/news/2024/6/10/gaza-conflict-latest-updates",   # Example extra link
    "https://www.reuters.com/world/us/us-election-2024-updates-2024-07-12/"   # Example extra link
]

# Extract info for all URLs
articles_data = [extract_article_info(url) for url in urls]

# Show results nicely
for article in articles_data:
    print("="*80)
    for key, value in article.items():
        print(f"{key}: {value}")
    print("\n")

# Save to CSV for later analysis
df = pd.DataFrame(articles_data)
df.to_csv("news_articles.csv", index=False)
print("Articles saved to news_articles.csv")
