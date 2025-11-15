from flair.data import Sentence
from flair.models import SequenceTagger

# Load model
tagger = SequenceTagger.load("ner")

# --- Function to run NER ---
def run_ner(text):
    sent = Sentence(text)
    tagger.predict(sent)
    print("Tagged:", sent.to_tagged_string())
    for ent in sent.get_spans('ner'):
        print(f"  Entity: {ent.text}, Type: {ent.get_label('ner').value}, Score: {ent.score:.4f}")
    print()

# Single example
run_ner("Barack Obama was the president of the United States.")

# Multiple sentences
examples = [
    "Elon Musk founded SpaceX and co-founded Tesla.",
    "Google is headquartered in Mountain View, California.",
    "Taylor Swift performed in Paris last week."
]

for txt in examples:
    print("Input:", txt)
    run_ner(txt)

# User input
user_txt = input("Enter a sentence: ")
run_ner(user_txt)
