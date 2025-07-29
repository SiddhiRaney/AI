import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Apple is looking at buying U.K. startup for $1 billion."

# Process the text
doc = nlp(text)

# Tokenization, POS, and Lemmatization
print("Tokens, POS tags, and Lemmas:")
for token in doc:
    print(f"{token.text:<12} | POS: {token.pos_:<10} | Lemma: {token.lemma_}")

# Named Entities
print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.text:<20} | Label: {ent.label_} ({spacy.explain(ent.label_)})")
