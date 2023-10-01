import time

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import winsound
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)  to  check which voice command use in this program (girl or boy)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")
    elif hour >= 16 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("i am Jimmy, tell me how may i help you!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        again = "say that again please..."
        print(again)
        speak(again)
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hello' in query:
            rand = ('Hello sir', "Good to see you again!")
            print(rand)
            speak(rand)

        elif 'hi ' in query:
            rand = ("Hi dear, how can I help?")
            print(rand)
            speak(rand)

        elif 'hey ' in query:
            repp = ('haaay buddy, nice to meet you')
            print(repp)
            speak(repp)

        elif 'hay ' in query:
            reppl = ('haaay buddy, nice to meet you')
            print(reppl)
            speak(reppl)

        elif 'doing' in query:
            reppl = ('i am waiting of your help!')
            print(reppl)
            speak(reppl)

        elif 'how are you' in query:
            reppl = ('i am splendid! , thank you for asking.')
            print(reppl)
            speak(reppl)

        elif 'age' in query:
            reppl = ("my age is 35 , but when i see you , my heart is sweet 18  ")
            print(reppl)
            speak(reppl)

        elif 'founded' in query:
            reppl = ("it depends on how you look at it. Mohit was founded in 26 january  2022.")
            print(reppl)
            speak(reppl)

        elif "what's your name" in query:
            reppl = ("My Name is  Jimmy, but You can call me Darling. you're  Darling")
            print(reppl)
            speak(reppl)

        elif 'tell me my name' in query:
            reppl = ("you're name is mine, only mine")
            print(reppl)
            speak(reppl)

        elif 'your instagram id' in query:
            reppp = "i am not using instagram , but my owner is using instagram , id is  ."
            print(reppp)
            speak(reppp)
            print('https://www.instagram.com/invites/contact/?i=1muezedv8otr5&utm_content=2lx8wks')

        elif 'bye' in query:
            reppl = ("Sad to  see you go :(", 'good bye  ')
            print(reppl)
            speak(reppl)
            exit()

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
            exit()

        elif 'open linkdin' in query:
            webbrowser.open('linkdin.com')
            exit()

        elif 'open github' in query:
            webbrowser.open('github.com')
            exit()

        elif 'open amazon' in query:
            webbrowser.open('amazon.com')
            exit()

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            exit()

        elif 'give me a compliment' in query:
            compliment = "when i listen your voice  ,  my mind sing a song "
            print(compliment)
            speak(compliment)
            songg = winsound.PlaySound('s.wav', winsound.SND_ASYNC)
            time.sleep(13)

        elif 'praise me' in query:
            compli = "when i see your picture   ,through my camera  , my heart says.. "
            print(compli)
            speak(compli)
            winsound.PlaySound('pr.wav', winsound.SND_ASYNC)
            time.sleep(15)

        elif 'go with me a date' in query:
            print('yeah sure , but im not a human :(')
            speak('yeah sure , but im not a human ')

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            print("playing...")
            pywhatkit.playonyt(song)
            exit()

        elif 'joke' in query:
            joke = (pyjokes.get_joke('en', 'all'))
            print(joke)
            speak(joke)
            laughter = winsound.PlaySound('santa_laugh.wav', winsound.SND_ASYNC)
            print(':) :) :) :) :)')
            time.sleep(2)

        elif 'open google' in query:
            webbrowser.open('google.com')
            exit()

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            exit()

        elif 'music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir the time is {strTime}")



        if 'quit' in query:
            print('Sad to  see you go :(",  "good bye"  ')
            speak('Sad to  see you go :(",  "good bye    "  ')
            exit()


