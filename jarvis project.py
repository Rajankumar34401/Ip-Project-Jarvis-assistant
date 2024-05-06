import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import pywhatkit
import openai
from hugchat import hugchat

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
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
        print("Say that again please...")  
        return "exit"
    return query

def chat_with_openai(query):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()


def chatBot(query):
    user_input=query.lower()
    chatbot=hugchat.ChatBot(cookie_path="cookies.json")
    id=chatbot.new_conversation()
    chatbot.change_conversation(id)
    response=chatbot.chat(user_input)
    print(response)
    return response


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play' in query:
            song = query.replace('play', '')
            pywhatkit.playonyt(song)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music = 'D:\\music'  # Change the directory as per your music folder
            songs = os.listdir(music)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "desktop open" in query:
            query = query.replace("desktop open", "")
            query = query.replace("jarvis", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\rajan\\AppData\\Local\\Programs\\Python\\python312\\jarvis project.py"
            os.startfile(codePath)

        elif 'shutdown' in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 1")

        elif 'logout' in query:
            speak("Logging out")
            os.system("shutdown -l")

        elif 'restart' in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 1")
            
        else:
            # Use the chatBot function for handling other queries
            response = chatBot(query)
            speak(response)

            exit()
