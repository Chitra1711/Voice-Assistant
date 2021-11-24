import pyttsx3
import tkinter
import json
import speech_recognition as sr
import datetime
import Wikipedia
import webbrowser
import os
import winshell
import pyjokes
import time
import requests
import shutil
from ecapture import ecapture as ec
from bs4 import BeautifulSoup

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  !")
 else:
      speak("Good Evening  !")
      assname = ("LEO")
     speak("I am your Assistant")
     speak(assname)

def usrname():
    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome ", uname.center(columns))
    print("#####################".center(columns))
   
speak("How can i Help you, ")

def takeCommand():
    r = sr.Recognizer()

 with sr.Microphone() as source:
print("Listening..."
 r.pause_threshold = 1
  audio = r.listen(source)
  try:
   print("Recognizing...")
   query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")

 except Exception as e:
   print(e)
    print("Unable to Recognize your voice.")
     return "None"
 
 return query

if _name_ == '_main_':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    usrname()

while True:
       query = takeCommand().lower()
           
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by VIT Students.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to VIT . further It's a secret")
       elif 'what is love' in query:
 speak("It is 7th sense that destroy all other senses")
         elif "who are you" in query:
            speak("I am your virtual assistant created by VIT Students")
        elif 'reason for you' in query:
            speak("I was created as a Minor project by CSBS Students ")
         elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
          speak("Recycle Bin Recycled")
       
elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop LEO from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Camera ", "img.jpg")

        elif "write a note" in query:
            speak("What should i write, ")
            note = takeCommand()
            file = open('LEO.txt', 'w')

         file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("LEO.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you ")
            speak(assname)
         elif "will you be my friend" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")
