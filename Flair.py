from flair.data import Sentence
from flair.models import SequenceTagger

# Load a pre-trained NER tagger
tagger = SequenceTagger.load("ner")

# Create a sentence
sentence = Sentence("Barack Obama was the president of the United States.")

# Run NER
tagger.predict(sentence)

# Print recognized entities
print(sentence.to_tagged_string())
