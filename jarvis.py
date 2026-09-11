import pyttsx3  #it is used to convert the text into voice
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
          print("Not Understand")
        
def speechtxt(x):
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[0].id)
            rate = engine.getProperty('rate')
            engine.setProperty('rate',190)
            engine.say(x)
            engine.runAndWait()
           
if __name__  == '__main__':

    # if sptext().lower() == "hey peter"
    data1=sptext().lower()

if "your name" in data1:
     name = " my name is peter"
     speechtxt(name)

elif "old are you" in data1:
     age = " am two years old"
     speechtxt(age)

elif 'time' in data1:
     time = datetime.datetime.now().strftime("%I%M%p")
     speechtxt
elif 'youtube' in data1:
    webbrowser.open("https://www.youtube.com/")
       
elif 'web' in data1:
     webbrowser.open("https://www.wscubetech.com/")

elif "joke" in data1:
     joke_1 = pyjokes.get_joke(language="en",category="neutral")
     speechtxt(joke_1)

elif 'play song' in data1:
     add = "/Users/ankuryadav/songs/1.mp3"
     listsong = os.listdis(add)
     print(listsong)
     os.startfile(os.path.join(add,listsong[0]))

 
