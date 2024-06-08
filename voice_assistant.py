import pyttsx3
import speech_recognition as s 
import webbrowser
import datetime
import pyjokes
import pyaudio
import os

# the below function converts speech to text
def st():
    r = s.Recognizer() # audio is begin recognized
    with s.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source) # remove noise from the audio
        a = r.listen(source)
        try:
            print("Recognizing...")
            data = r.recognize_google(a)
            print(data)
            return data
        except s.UnknownValueError:
            print("Not Understand")
            
# the below function converts text to speech
def ts(x):
    e = pyttsx3.init()
    v = e.getProperty('voices')
    e.setProperty('voice',v[0].id)
    r = e.getProperty('rate')
    e.setProperty('r',150)
    e.say(x)
    e.runAndWait()

if __name__ == '__main__':
    while True:
        d1 = st().lower()

        if "your name" in d1:
            n = " My name is Ayush"
            ts(n)
        elif "old are you" in d1:
            a = " I am 21 years old"
            ts(a)
        elif "time" in d1:
            t = datetime.datetime.now().strftime("%I%M%P")
            ts(t)
        elif "youtube" in d1:
            webbrowser.open("https://www.youtube.com/")
        elif "website" in d1:
            webbrowser.open("https://www.python.org/")
        elif "joke" in d1:
            j = pyjokes.get_joke(language="en",category="all")
            print(j)
            ts(j)
        elif "play song" in d1:
            add = "*****" # give path of the songs where it is saved
            ls = os.listdir(add)
            print(ls)
            os.startfile(os.path.join(add,ls[1]))
        elif "exit" in d1:
            ts("thank you")
            break