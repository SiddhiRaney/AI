from transformers import pipeline

# Load the sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")

# List of texts to classify
texts = [
    "I love using Hugging Face Transformers! It's so powerful and easy.",
    "I'm not sure how I feel about this product.",
    "This is the worst experience I've ever had.",
    "Absolutely fantastic! Highly recommend it to everyone.",
    "It was okay, nothing special."
]

# Perform classification on all texts
results = classifier(texts)

# Print results with text and its label
for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})\n")
