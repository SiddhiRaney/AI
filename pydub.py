from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize, speedup, low_pass_filter, high_pass_filter

# Load an audio file
song = AudioSegment.from_file("song.mp3", format="mp3")

# ----------------------
# Basic operations
# ----------------------
first_10_sec = song[:10000]                     # First 10 seconds
mid_10_sec = song[10000:20000]                 # 10-20 seconds
louder = song + 6                               # Increase volume
faded = song.fade_in(2000).fade_out(3000)      # Fade in/out
reversed_song = song.reverse()                 # Reverse audio
normalized_song = normalize(song)              # Normalize volume
channels = song.split_to_mono()                # Split stereo
left_channel = channels[0]
right_channel = channels[1]
combined = first_10_sec + mid_10_sec           # Concatenate segments
overlayed = first_10_sec.overlay(mid_10_sec)  # Overlay two segments
faster = speedup(song, playback_speed=1.5)    # Speed up
slower = speedup(song, playback_speed=0.75)   # Slow down

# ----------------------
# Advanced operations
# ----------------------
# 1. Echo effect (simple version)
def add_echo(sound, delay=500, decay=0.5):
    echo = sound[:0]  # empty audio segment
    for i in range(0, len(sound), delay):
        segment = sound[i:i+delay] - (i // delay) * decay * 10
        echo = echo + segment
    return sound.overlay(echo)

echoed = add_echo(song)

# 2. Low-pass and high-pass filters
low_passed = low_pass_filter(song, cutoff=400)     # remove high frequencies
high_passed = high_pass_filter(song, cutoff=2000)  # remove low frequencies

# 3. Pitch shift by changing frame rate
def pitch_shift(sound, semitones):
    new_rate = int(sound.frame_rate * (2 ** (semitones / 12)))
    return sound._spawn(sound.raw_data, overrides={"frame_rate": new_rate})

pitch_up = pitch_shift(song, 3)   # shift up by 3 semitones
pitch_down = pitch_shift(song, -3)  # shift down by 3 semitones

# 4. Reverse fade effect
reverse_fade = song.reverse().fade_in(2000).fade_out(2000)

# 5. Overlay with volume adjustment
overlay_louder = first_10_sec.overlay(mid_10_sec + 6)

# ----------------------
# Export all variations
# ----------------------
faded.export("faded.wav", format="wav")
overlayed.export("overlayed.wav", format="wav")
reversed_song.export("reversed.wav", format="wav")
faster.export("faster.wav", format="wav")
slower.export("slower.wav", format="wav")
normalized_song.export("normalized.wav", format="wav")
left_channel.export("left_channel.wav", format="wav")
right_channel.export("right_channel.wav", format="wav")
combined.export("combined.wav", format="wav")
echoed.export("echoed.wav", format="wav")
low_passed.export("low_passed.wav", format="wav")
high_passed.export("high_passed.wav", format="wav")
pitch_up.export("pitch_up.wav", format="wav")
pitch_down.export("pitch_down.wav", format="wav")
reverse_fade.export("reverse_fade.wav", format="wav")
overlay_louder.export("overlay_louder.wav", format="wav")

# ----------------------
# Play previews
# ----------------------
play(first_10_sec)
play(echoed)
play(pitch_up)
