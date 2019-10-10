from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from playsound import playsound

def speak(query):
    #tts = gTTS(text=query, lang='en-IN')
    #tts.save("query.mp3")
    #playsound('query.mp3')

    engine = pyttsx3.init() 
    engine.setProperty('voice', 'english+f2')
    engine.setProperty('rate', 160)    # Speed percent (can go over 100)
    engine.setProperty('volume', 2.0)
    engine.say(query) 
    engine.runAndWait()   
       

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        #r.pause_threshold = 1
        print("Listening....")
        audio = r.listen(source)
        #print("m done ")
    
    try :
        print("Recognizing....")
        query =r.recognize_google(audio,language='en-in')
        print("user said : ",query)
        #speak(query)
    
    except Exception :
        print("Say that again please !! ")
        return "none"
    return query


#query = takecommand().lower()
#speak(query)