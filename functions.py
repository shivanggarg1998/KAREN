
import speakandrecognize as sar
import datetime
import wikipedia
import random
import os

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        sar.speak("Good morning ! ")
    elif hour>=12 and hour <18:
        sar.speak("Good aftenoon ! ")
    else:
        sar.speak("Good evening! ")
    sar.speak("It's Karen. How may i help you ?")


def wiki(query):
    try:
        print("Searching on Wikipedia.....")
        sar.speak('Searching on Wikipedia.....')
        
        query = query.replace("search","")
        query = query.replace("wikipedia","")
        query = query.replace("on","")

        results = wikipedia.summary (query,sentences=2)
        sar.speak("According to wikipedia - ")
        sar.speak(results)
    except :
        print("error- KAREN did not recognized what you said ")
        sar.speak("Didn't get that. Say that again!")
def tellMeAJoke():
    sar.speak("A bear walks into a bar and says, Give me a whiskey and … cola. Why the big pause? asks the bartender. The bear shrugged. I’m not sure; I was born with them.")
    
