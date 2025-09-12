from sacremoses import MosesTokenizer, MosesDetokenizer

# Initialize tokenizer and detokenizer
tokenizer = MosesTokenizer(lang='en')
detokenizer = MosesDetokenizer(lang='en')

# Example texts
texts = [
    "Hello, how are you doing today?",
    "I'm learning Python—it's really fun!",
    "Mr. Smith bought 3.5kg of apples... amazing, right?"
]

for i, text in enumerate(texts, 1):
    print(f"\n--- Example {i} ---")
    print("Original:", text)

    # Tokenize with options
    tokens = tokenizer.tokenize(text, escape=False, aggressive_dash_splits=True)
    print("Tokens:", tokens)

    # Detokenize
    detext = detokenizer.detokenize(tokens)
    print("Detokenized:", detext)

# Batch tokenization
print("\n--- Batch Tokenization ---")
batch_tokens = tokenizer.batch_tokenize(texts)
for i, token_list in enumerate(batch_tokens, 1):
    print(f"Sentence {i} tokens:", token_list)

# Batch detokenization
print("\n--- Batch Detokenization ---")
batch_detexts = [detokenizer.detokenize(toks) for toks in batch_tokens]
for i, detext in enumerate(batch_detexts, 1):
    print(f"Sentence {i} detokenized:", detext)
