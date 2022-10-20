from  gtts import gTTS
import os
tts= gTTS(text="my heart is all you",lang="en")
filename="hello.mp3"
tts.save(filename)
os.system(f"start {filename}")