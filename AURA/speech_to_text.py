import speech_recognition as sr
from requests_html import HTMLSession
import text_to_speech

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ask Anything...")
        audio = r.listen(source)

        try:
            voice_data = r.recognize_google(audio)
            return voice_data

        except sr.UnknownValueError:
            text_to_speech.text_to_speech("Sorry, I did not understand")
        except sr.RequestError:
            text_to_speech.text_to_speech("No internet connection, please turn on your internet")


# ✅ Call the function and display the result
if __name__ == "__main__":
    result = speech_to_text()
    if result:
        print("You said:", result)
        text_to_speech.text_to_speech("You said " + result)
