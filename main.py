from gtts import gTTS
import os
import webbrowser
import setuptools
import speech_recognition as sr
import pyaudio

lib = {"playlist":"https://open.spotify.com/playlist/1sa9vCszGV1rfMoecrwFFc?si=cece591cb9c341a2","blinding lights":"https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b?si=18c60f6537a3471b"}

def speak(str):
    tts = gTTS(str , lang="en")
    tts.save("hello.mp3")
    os.system("afplay hello.mp3")
    
def process(str):
    if "open youtube" in str.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in str.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in str.lower():
        webbrowser.open("https://www.linkedin.com")

def music(str):
    speak("Welcome to music library")
    if "playlist" in str.lower():
        speak("Playing your playlist")
        webbrowser.open(lib["blinding lights"])

# Speech Hearing
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source , timeout = 2 , phrase_time_limit = 2)
    
# Speech Recognition  
try:
    command = recognizer.recognize_google(audio)
    print(command)
except Exception as e:
    speak("Can't hear sorry")
    command = ""
    

if "alexa" in command.lower():
    speak("Ya")
    while(True):
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognizer.listen(source , timeout = 3 , phrase_time_limit = 3)
        
        try:
           command = recognizer.recognize_google(audio)
           
        except Exception as e:
           print("Cant hear sorry")
           command = ""
           
        if "music" in command.lower():
            music("playlist")
        else:
            process(command)

   
   
 
    
# tts = gTTS("Yo Yo Yo 1 4 8, 3 to the 3 to the 6 to the 9, representing the ABQ, What Up Biaatch, Leave it to the tone",lang="en",tld="com.au")
# tts.save("hello.mp3")
# os.system("afplay hello.mp3")
# tt2 = gTTS("Yeahh I am Jesse")
# tt2.save("hello.mp3")
# os.system("afplay hello.mp3")