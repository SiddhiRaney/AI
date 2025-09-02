from sacremoses import MosesTokenizer, MosesDetokenizer

# Initialize tokenizer and detokenizer
tokenizer = MosesTokenizer(lang='en')
detokenizer = MosesDetokenizer(lang='en')

# Tokenize text
text = "Hello, how are you doing today?"
tokens = tokenizer.tokenize(text)
print(tokens)

# Detokenize back
detext = detokenizer.detokenize(tokens)
print(detext)
