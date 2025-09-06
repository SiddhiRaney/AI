from pydub import AudioSegment
from pydub.playback import play

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

# -------------------------------------
# Additional operations
# -------------------------------------

# Cut from 10 to 20 seconds
mid_10_sec = song[10000:20000]

# Overlay audio (mixing two segments)
overlayed = first_10_sec.overlay(mid_10_sec)

# Reverse audio
reversed_song = song.reverse()

# Change speed (faster/slower by changing frame rate)
faster = song._spawn(song.raw_data, overrides={"frame_rate": int(song.frame_rate * 1.5)})
slower = song._spawn(song.raw_data, overrides={"frame_rate": int(song.frame_rate * 0.75)})

# Normalize volume
normalized = song.apply_gain(-song.max_dBFS)

# Split stereo to mono channels
channels = song.split_to_mono()
left_channel = channels[0]
right_channel = channels[1]

# Combine two songs (concatenate)
combined = first_10_sec + mid_10_sec

# Export all variations
overlayed.export("overlayed.wav", format="wav")
reversed_song.export("reversed.wav", format="wav")
faster.export("faster.wav", format="wav")
slower.export("slower.wav", format="wav")
normalized.export("normalized.wav", format="wav")
left_channel.export("left_channel.wav", format="wav")
right_channel.export("right_channel.wav", format="wav")
combined.export("combined.wav", format="wav")

# Play a preview directly
play(first_10_sec)
