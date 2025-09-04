from pydub import AudioSegment

# Load an audio file (requires ffmpeg installed)
song = AudioSegment.from_file("song.mp3", format="mp3")

# Cut first 10 seconds
first_10_sec = song[:10000]

# Increase volume by +6 dB
louder = song + 6

# Fade in and fade out
faded = song.fade_in(2000).fade_out(3000)

# Export back as WAV
faded.export("output.wav", format="wav")
