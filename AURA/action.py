import pyttsx3
import datetime
import os
import webbrowser
import weather  
import text_to_speech
import speech_to_text

def handle_user_input(user_data): 

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is AURA Artificial Unified Responsive Assistant)")
        return "my name is aura"
    
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("hello, how can I help you?")
        return "hello, how can I help you?"
    
    elif "how are you" in user_data:
        text_to_speech.text_to_speech("I am fine, thank you")
        return "i am fine, thank you"
    
    elif "what is the time" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} hours and {current_time.minute} minutes"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("Playing music")
        return "playing music"
    
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("opening YouTube")  
        return "opening YouTube"
    
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("opening Google")  
        return "opening Google"
    
    elif "what is the weather" in user_data and (ans := weather.weather()):
        weather_report = f"The weather is {ans['description']}, temperature is {ans['temp']}°C and humidity is {ans['humidity']}%"
        text_to_speech.text_to_speech(weather_report)
        return weather_report

    
    elif "shut down" in user_data:
        text_to_speech.text_to_speech("shutting down, goodbye")
        return "shutting down, goodbye"
    
    else:
        text_to_speech.text_to_speech("sorry i didn't understand ")
        return "sorry i didn't understand "