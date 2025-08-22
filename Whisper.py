import openai
import os

# Load your API key
openai.api_key = "your_api_key_here"

def transcribe_audio(file_path, save_output=True, translate=False):
    """
    Transcribe audio using OpenAI's Whisper model.
    
    Args:
        file_path (str): Path to the audio file
        save_output (bool): Save transcription to a text file
        translate (bool): If True, translates to English
    """
    try:
        # Open the audio file
        with open(file_path, "rb") as audio_file:
            if translate:
                print("Translating audio to English...")
                transcript = openai.Audio.translations.create(
                    model="whisper-1",
                    file=audio_file
                )
            else:
                print("Transcribing audio...")
                transcript = openai.Audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )

        # Print transcript text
        print("\n--- Transcript ---\n")
        print(transcript.text)

        # Save transcript to a .txt file
        if save_output:
            output_file = os.path.splitext(file_path)[0] + "_transcript.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(transcript.text)
            print(f"\n✅ Transcript saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with your actual audio file path
    audio_path = "audio_sample.mp3"  # <-- change this to your file
    transcribe_audio(audio_path, save_output=True, translate=False)
