import webbrowser
import pyjokes
import pyttsx3
import speech_recognition as sr
import datetime
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            #print(data)
            return data
        except sr.UnknownValueError:
            print("Couldn't Understand")
            
def txttsp(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if 'hey jarvis' in sptext().lower():
        txttsp("jarvis activating")
        while True:
            data1= sptext().lower()
            if "your name" in data1:
                name = "my name is Jarvis"
                txttsp(name)
            elif "old are you" in data1:
                age = "I am two years old"
                txttsp(age)
            elif "time" in data1:
                print("Current Time")
                time1 = datetime.datetime.now().strftime("%I%M%p")
                txttsp(time1)
            elif "youtube" in data1:
                print("Opening Youtube")
                youtube="Opening youtube"
                txttsp(youtube)
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                print("Joke of the day")
                joke = pyjokes.get_joke(language="en",category="neutral")
                txttsp(joke)
                print(joke)
            elif 'play song' in data1:
                print("Playing Song")
                song = "Playing Song"
                txttsp(song)
                add = r"C:\Users\Sadiya_\Music"
                #listsong = os.listdir(add)
                #print(listsong)
                os.startfile(os.path.join(add))
            elif "exit" in data1:
                txttsp("Thank You for exploring me")
                print("Thank You")
                break
            time.sleep(5)
    else:
        print("Thanks")
    
    
    
    

