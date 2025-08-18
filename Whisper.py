import openai

# Make sure you have installed openai package:
# pip install openai

# Load your API key
openai.api_key = "your_api_key_here"

# Open an audio file (e.g., mp3, wav, m4a)
with open("audio_sample.mp3", "rb") as audio_file:
    transcript = openai.Audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

print(transcript.text)
