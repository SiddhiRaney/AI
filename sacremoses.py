from sacremoses import MosesTokenizer, MosesDetokenizer, MosesTruecaser, MosesPunctNormalizer

# Initialize tools
tokenizer = MosesTokenizer(lang='en')
detokenizer = MosesDetokenizer(lang='en')
truecaser = MosesTruecaser()
normalizer = MosesPunctNormalizer(lang='en')

# Example texts
texts = [
    "Hello, how are you doing today?",
    "I'm learning Python—it's really fun!",
    "Mr. Smith bought 3.5kg of apples... amazing, right?",
    "THIS IS AN ALL CAPS SENTENCE!",
    "don't stop-believing; keep moving forward..."
]

for i, text in enumerate(texts, 1):
    print(f"\n--- Example {i} ---")
    print("Original:", text)

    # Normalize punctuation
    normalized = normalizer.normalize(text)
    print("Normalized:", normalized)

    # Tokenize
    tokens = tokenizer.tokenize(normalized, escape=False, aggressive_dash_splits=True)
    print("Tokens:", tokens)

    # Truecase (simulate training by fitting on the current texts)
    truecaser.train([tokens])  # usually you'd train on a large corpus
    truecased_tokens = truecaser.truecase(tokens)
    print("Truecased Tokens:", truecased_tokens)

    # Detokenize
    detext = detokenizer.detokenize(truecased_tokens)
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

# Demonstrating escape option
print("\n--- Tokenization with Escape ---")
for i, text in enumerate(texts, 1):
    tokens = tokenizer.tokenize(text, escape=True)
    print(f"Sentence {i} escaped tokens:", tokens)

# Demonstrating aggressive dash splits
print("\n--- Aggressive Dash Splits ---")
sample_text = "well-known facts about state-of-the-art models"
tokens_dash = tokenizer.tokenize(sample_text, aggressive_dash_splits=True)
print("Original:", sample_text)
print("Tokens with aggressive dash splits:", tokens_dash)
print("Detokenized back:", detokenizer.detokenize(tokens_dash))
