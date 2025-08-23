import openai
import os
import json

# Load API key from environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY", "your_api_key_here")

def transcribe_audio(
    file_path: str,
    save_output: bool = True,
    output_format: str = "txt",
    translate: bool = False,
    language: str = None,
    output_file: str = None
) -> str:
    """
    Transcribe or translate audio using OpenAI's Whisper model.
    
    Args:
        file_path (str): Path to the audio file
        save_output (bool): Save transcription to a file
        output_format (str): 'txt' or 'json'
        translate (bool): If True, translates audio into English
        language (str): Force transcription in a specific language (e.g., 'en', 'hi', 'fr')
        output_file (str): Custom output filename
        
    Returns:
        str: Transcript text
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "rb") as audio_file:
            print("🎧 Processing audio...")

            if translate:
                print("🌍 Translating audio to English...")
                transcript = openai.Audio.translations.create(
                    model="whisper-1",
                    file=audio_file
                )
            else:
                print("📝 Transcribing audio...")
                transcript = openai.Audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language=language
                )

        text_output = transcript.text.strip()
        print("\n--- Transcript ---\n")
        print(text_output)

        if save_output:
            if not output_file:
                base_name = os.path.splitext(file_path)[0]
                output_file = f"{base_name}_transcript.{output_format}"

            if output_format == "txt":
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(text_output)
            elif output_format == "json":
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(transcript, f, indent=4, ensure_ascii=False)
            else:
                raise ValueError("Unsupported output format. Use 'txt' or 'json'.")

            print(f"\n✅ Transcript saved to: {output_file}")

        return text_output

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


# Example usage
if __name__ == "__main__":
    audio_path = "audio_sample.mp3"  # <-- change this to your file
    
    # Call function with multiple options
    result = transcribe_audio(
        audio_path,
        save_output=True,
        output_format="json",   # options: "txt", "json"
        translate=False,
        language=None           # e.g., "en", "hi", "fr"
    )
