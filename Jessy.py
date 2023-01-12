from email.mime import audio
from http import server
import imp
from logging import exception
import smtplib
import webbrowser
import pyttsx3                  #pip install pyttsx3
import datetime
import speech_recognition as sr     #pip install speech_recognition     #--> Same comadn for all pakages
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import sys
import random

# dic = dict()
# dic = {'pinke':'+919503907181', 'aayan':'+917385970879' }


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=8 and hour<12:
        speak("Good Mornig!")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<20:
        speak("Good evining!")
    else:
        speak("Good Night")

    print("-------- I am Jessy assistant of aakash sir. Plese may i know who is speaking with me. ---------")
    speak("I am Jessy assistant of aakash. Plese may i know who is speaking with me.")
    

def takeCommand():
    # """It takes Microphone input from the user and returns string Output"""
    
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognzeing...")
        speak("Recognzeing Wait")
        query = r.recognize_google(audio,language='en.in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Sorry about that. i didnt here anything plese speak again...\n")
        speak("Sorry about that. i didnt here anything plese speak again")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.helo()
    server.starttls()
    server.login('aakashmohole@gmail.com','aakashA415')
    server.sendmail("aakashmohole@gmail.com",to, content)
    server.close()
    

if __name__ == '__main__':
    # speak("Hellow Aakash Sir")
    wishMe()

    while True:
        query = takeCommand().lower()

        #Logic for executing tasks

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            # print(results)
        
        elif'Hey Jessy' in query:
            speak("Checking identity plese wait.")
            speak("Accsess Granted. honer to meet you Aakash. how can i help you")
        
        elif'i am' in query:
            speak("Accsess Granted. honer to meet you sir. how can i help you")

        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open google' in query:
            print("sir, what should i search on google")
            speak("sir, what should i search on google")
 
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif'open whatsapp web' in query:
            webbrowser.open("web.whatsapp.com")

        elif'play music' in query:
            music_dic= 'F:\\Music'
            songs = os.listdir(music_dic)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dic,rd))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif'open sublime' in query:
            sublimPath = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
            os.startfile(sublimPath)
        
        elif'open notepad' in query:
            notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(notepadPath)

        elif 'who are you' in query:
            speak("I am Jessy. personal desktop assistent of Mr aakash mohole. with version 3.10. plese tell me what i can do for you. ")
            print("I am Jessy. personal desktop assistent of Mr aakash mohole. with version 3.10. plese tell me what i can do for you. ")

        elif 'message' in query:
            try:
                # speak("sir, plese tell me number")
                # print("sir, plese tell me number")
                # who=takeCommand().isnumeric()
                speak("sir, what shoul i say")
                print("sir, what shoul i say")
                cm=takeCommand().lower()
                kit.sendwhatmsg("+917385970879",f"{cm}",23,45)
            except Exception as e:
                print(e)
                speak("i am not able to diliver this message.")


    #Email modul not working - 
        elif 'email' in query:
            try:
                speak("what shoud i say")
                print("what shoud i say")
                content= takeCommand()
                to = "aakashmohole@gmail.com"
                sendEmail(to, content)
                speak("Email is succesfully send.")
            except Exception as e:
                print(e)
                speak("I am not able to send this mail.")


    #exit step
        elif("exit") in query:
            speak("Thansk for using me sir, Have a good day.")
            sys.exit()









