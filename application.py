import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import time
from time import ctime
import re
import webbrowser
import smtplib
import bs4
import requests


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio = r.listen(source,phrase_time_limit = 10)
    data=""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data

def respond(String):
    print(String)
    tts = gTTS(text=String,lang="en")
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")

def voice_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well")
        
    if "what is your name" in data:
        listening = True
        respond("Myself Alexamani")
        
    if "who are you" in data:
        listening = True
        respond("I am Virtual Assistant")
        
    if "why virtual girlfriend" in data:
        listening = True
        respond("Because i will help you to make your life simple")
        
        
    if "time" in data:
        listening  = True
        respond(ctime())

    if "open google" in data.casefold():
        listening =True
        reg_ex = re.search('open google(.*)',data)
        url = 'https://www.google.com/'
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        print('Done')
        respond('Done')

    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'sakethreddy.kallepu@gmail.com','just':'ravichandra178@gmail.com'}
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person")
        message = listen()
        content = 'Subject: {}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)

        #identify the server
        mail.ehlo()

        mail.starttls()

        #login
        mail.login('qwertyforwork@gmail.com','jyppeoscgghmqlbf')

        mail.sendmail('qwertyforwork@gmail.com',toaddr,content)

        mail.close()

        respond('Email Sent')

    if "wiki" in data.casefold():
        listening = True
        respond("What should I search?")
        query = listen()
        response = requests.get("https://en.wikipedia.org/wiki/" +query)
        if response is not None:
            html = bs4.BeautifulSoup(response.text,'html.parser')
            paragraphs = html.select("p")
            intro = [i.text for i in paragraphs]
            halo = ''.join(intro)
        respond(halo[:200])

    if "ok bye" in data:
        listening = False
        print("Listening Stopped")
        respond("Bye, Vinay I Love You ")

    try:
        return listening
    except UnboundLocalError:
        print("TimedOut-->Re-Launch")
        
    
time.sleep(2)
respond("Hello Vinay,what can I do for you?")
listening = True
while listening == True:
    data = listen() #calling the listen()
    listening = voice_assistant(data)
    
    
    
    
