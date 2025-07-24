from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text = """
Artificial Intelligence (AI) is the simulation of human intelligence in machines 
that are programmed to think like humans and mimic their actions. The term may also 
be applied to any machine that exhibits traits associated with a human mind such as 
learning and problem-solving.
"""

# Parse text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Create LSA summarizer
summarizer = LsaSummarizer()

# Generate summary (e.g., 2 sentences)
summary = summarizer(parser.document, 2)

# Print summary
for sentence in summary:
    print(sentence)
