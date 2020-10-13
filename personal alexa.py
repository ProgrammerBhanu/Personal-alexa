import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhanusolankiboy786@gmail.com', '97208985')
    server.sendmail('bhanusolankiboy786@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'knowledge decoder' in query:
            webbrowser.open("knowledgedecoder.in")

        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to bhanu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "solankiboy9561@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend bhanu bhai. I am not able to send this email")
        elif 'ms word' in query:
             codePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
             os.startfile(codePath)
        elif 'chrome' in query:
            ch_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ch_path)
        elif 'play music' in query:
            music_dir = 'E:\\new song'
            songs = os.listdir(music_dir)
            print(songs)
            random_songs=random.choice(songs)
            os.startfile(os.path.join(music_dir, random_songs))
        elif 'pycharm' in query:
            py_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\pycharm64.exe"
            os.startfile(py_path)
        elif 'my pc' in query:
            fe_path="C:\\Windows\\explorer.exe"
            os.startfile(fe_path)
        # elif 'setting' in query:
        #     setting_pah=
        #     os.startfile(setting_pah)