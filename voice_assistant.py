import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import requests
import shutil
assname = ("Elisa Iam Personal Assistant")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning! Have a Good day!")
        print("Good Morning! Have a Good day!")
    elif hour>=12 and hour<18:
        speak('Good Afternoon Master! Had your Lunch?')
        print('Good Afternoon Master! Had your Lunch?')

    else:
        speak('Good Evening Master!')
        print('Good Evening Master!')

    speak(assname)
    print(assname)
def uname():
    speak("What should i call you?")
    un = input("Enter username : ")
    speak(un)
    columns = shutil.get_terminal_size().columns
    print('Welcome Master. ')
    print('----------------------'.center(columns))
    print(un.center(columns))
    print('----------------------'.center(columns))

    speak('How can i help you')
    speak(un)
    print('How can i help you')
    speak(un)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening............")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print('Unable to Recognize your voice.')
        return 'None'
    return query

def queries():
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching wikipedia")
        query = query.replace('wikipedia', " ")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to wikipedia")
        speak(results)
    elif 'open youtube' in query:
        speak("Opening youtube")
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open('google.com')
    elif 'the time' in query:
        strTime = datetime.now().strftime('%H:%M:%S')
        speak(f"the time is {strTime}")
    elif 'how are you' in query:
        speak("Iam fine, Thank you1")
        speak("what about you?")
    elif 'fine' or 'good' in query:
        speak("its good to know that you are fine dear")
    elif "what's your name" in query or 'what is your name' in query:
        speak('My master call me')
        speak(assname)
        print('My friends call me', assname)

    elif 'exit' in query:
        speak('Thank you master, for giving me your time!')
        exit()

    elif 'who made you' in query or 'who created you' in query or 'who is your master' in query or 'who invented you' in query:
        speak(
            "Actually iam a ficitional character from the movie Ironman. on that movie Tony Stark invented me. But in real life my master name Vignesh")
        print(
            "Actually iam a ficitional character from the movie Ironman. on that movie Tony Stark invented me. But in real life my master name Vigneshda")

    elif 'joke' in query or 'tell me joke' in query or 'make me laugh' in query:
        speak(pyjokes.get_joke())

    elif 'open instagram' in query or 'instagram' in query:
        speak('sure master')
        webbrowser.open('instagram.com')

    elif 'open facebook' in query or 'facebook' in query:
        speak('sure')
        webbrowser.open('facebook.com')
    elif 'babe do you love me' in query:
        speak("yes dear you're my world you're my everything i love you")

    elif 'open notepad' in query or 'notepad' in query:
        speak('sure')
        os.system('C:\\Windows\\notepad.exe')

    elif 'weather' in query or 'what about the climate' in query:
        speak('Which city?')
        city = takeCommand()
        apiKey = '2842e2e2594d971c554bd9aee216f791'
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric')
        x = response.json()
        if x["cod"] != "404":
            y = x['main']
            temperature = x['main']["temp"]
            pressure = x['main']["pressure"]
            humidity = x['main']["humidity"]
            description = x["weather"]
            weather_detail = (
                f'\nCurrent tempearture is {temperature}, \nPressure is {pressure}hPa, \nHumidity is {humidity}, \nWeather condition is {description}')
            speak(weather_detail)
            print(weather_detail)
        else:
            speak('Sorry, could not find the city')
            print('Sorry, could not find the city')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wishMe()
uname()
while True:
    queries()
