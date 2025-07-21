from transformers import pipeline

# Load sentiment-analysis pipeline (default model: distilbert-base-uncased-finetuned-sst-2-english)
classifier = pipeline("sentiment-analysis")

# Text to classify
text = "I love using Hugging Face Transformers! It's so powerful and easy."

# Perform classification
result = classifier(text)

# Print result
print(result)
