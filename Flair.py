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

# --- Loop for continuous user input ---
print("\n--- Interactive NER Mode (type 'exit' to stop) ---")
while True:
    user_txt = input("Enter a sentence: ")
    if user_txt.lower() == "exit":
        print("Exiting interactive mode...\n")
        break
    run_ner(user_txt)


# --- NER on lines from a text file ---
def run_ner_on_file(in_file, out_file):
    try:
        with open(in_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        results = []
        print(f"\nRunning NER on file: {in_file}\n")

        for line in lines:
            line = line.strip()
            if not line:
                continue
            sent = Sentence(line)
            tagger.predict(sent)
            ents = sent.get_spans('ner')

            # Print
            print("Input :", line)
            print("Tagged:", sent.to_tagged_string())
            for e in ents:
                print(f"  Entity: {e.text}, Type: {e.get_label('ner').value}, Score: {e.score:.4f}")
            print()

            # Save to list
            for e in ents:
                results.append(f"{line} || {e.text} || {e.get_label('ner').value} || {e.score:.4f}")

        # Write results
        with open(out_file, "w", encoding="utf-8") as f:
            for r in results:
                f.write(r + "\n")

        print(f"✔ Output saved to: {out_file}\n")

    except FileNotFoundError:
        print(f"Error: File '{in_file}' not found.\n")


# Example usage:
# run_ner_on_file("input.txt", "ner_output.txt")
