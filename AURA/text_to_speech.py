import pyttsx3
def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 100) 
    voices = engine.getProperty('voices')
    engine.say(text)
    engine.runAndWait()
