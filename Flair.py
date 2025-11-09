# Import necessary modules from Flair
from flair.data import Sentence
from flair.models import SequenceTagger

# Step 1: Load a pre-trained Named Entity Recognition (NER) model
# "ner" is a general English NER model included with Flair
tagger = SequenceTagger.load("ner")

# Step 2: Create a sentence object that you want to analyze
sentence = Sentence("Barack Obama was the president of the United States.")

# Step 3: Run the NER model on the sentence
tagger.predict(sentence)

# Step 4: Print the sentence with recognized entities highlighted
# This shows entities like PERSON, LOCATION, ORGANIZATION, etc.
print("Tagged sentence:", sentence.to_tagged_string())

# Step 5: Iterate over the entities for detailed information
print("\nDetailed entity information:")
for entity in sentence.get_spans('ner'):
    print(f"Entity: {entity.text}, Type: {entity.get_label('ner').value}, Score: {entity.score:.4f}")
