from gtts import gTTS
text = "Welcome to python coding with Edwin "
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")
print("Successfully saved into the file ")
