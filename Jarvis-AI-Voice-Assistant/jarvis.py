import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        print("Hi there, Good Morning!")
        speak("Hi there, Good Morning!")
    elif 12 <= hour < 18:
        print("Hi there, Good Afternoon!")
        speak("Hi there, Good Afternoon!")
    else:
        print("Hi there, Good Evening!")
        speak("Hi there, Good Evening!")

    print("I am Jarvis. How can I help you today?\n")
    speak("I am Jarvis. How can I help you today?")

def takecommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")
        return query.lower()

    except Exception as e:
        print("Say that again please...")
        return "None"

def main():
    wishme()
    while True:
         query = takecommands()

         # Logic for executing commands based on request

         # Wikipedia
         if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

         # To open websites
         elif 'open youtube' in query:
             speak("Opening youtube...")
             webbrowser.open('https://www.youtube.com/')

         elif 'open google' in query:
             speak("Opening google...")
             webbrowser.open('https://www.google.com/')

         elif 'open' in query and ('.com' in query or '.in' in query):
            query = query.replace('open ', '')
            speak(f"Opening {query}...")
            webbrowser.open(query)

         # To play random music
         elif 'play music' in query:
             music_dir = 'F:\\Music\\Kannada Melodies🎵'
             songs = [song for song in os.listdir(music_dir)
                      if song.endswith(('.mp3', '.wav')) and song.lower() != 'desktop.ini']
             if len(songs) > 0:
                 random_song = random.choice(songs)
                 speak("Playing Music...")
                 os.startfile(os.path.join(music_dir, random_song))
             else:
                 speak("Not enough music files in the directory or no files with the specified file types.")

         # To convey Date and time
         elif 'the time' in query or 'what time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             print(strTime)
             speak(f"The time is {strTime}")

         elif 'day' in query or 'date' in query:
             strDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
             print(strDate)
             speak(f"Today is {strDate}")

         # Open Applications
         elif 'chrome' in query or 'browser' in query:
             chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
             speak("Opening browser")
             os.startfile(chrome_path)

         elif 'file explorer' in query:
             FE = 'C:\\'
             speak("Opening file explorer")
             os.startfile(FE)

         elif 'open camera' in query:
             speak("Opening camera")
             cap = cv2.VideoCapture(0)
             
             if not cap.isOpened():
                err = 'Error: Could not open webcam.'
                print(err)
                speak(err)
                exit()
             
             speak("Camera opened successfully. Press 'q' to close.")
             while True:
                ret, frame = cap.read()
                cv2.imshow('Camera', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
             cap.release()
             cv2.destroyAllWindows()

         # Others
         elif any(word in query for word in ['hi', 'hello', 'hey jarvis']):
             print("Hi there! What's up?\n")
             speak("Hi there! What's up?")

         elif 'how are you' in query:
             print("I am doing great! How about you?\n")
             speak("I am doing great! How about you?")

         elif any(word in query for word in ['good', 'great', 'amazing', 'fine', 'wonderful', 'fantastic', 'surprising']):
             print("Sounds good to hear from you. What can I assist you with?\n")
             speak("Sounds good to hear from you. What can I assist you with?")

         elif 'what is your name' in query or "what's your name" in query:
             print('My name is Jarvis. I am here to assist you. Please feel free to command me!\n')
             speak('My name is Jarvis. I am here to assist you. Please feel free to command me!')

         elif 'thanks' in query or 'thank you' in query:
             print("My pleasure!. I am always there to help you.\n")
             speak("My pleasure!. I am always there to help you.")

         elif 'who made you' in query or 'who created you' in query or 'who programmed you' in query:
              print("It's Franklin, who developed me, and i am glad to be assisting you through him.\n")
              speak("It's Franklin, who developed me, and i am glad to be assisting you through him.")

         # Quit Jarvis
         elif any(word in query for word in ['quit', 'exit', 'close', 'bye','bye jarvis']):
             print("Bye!. Have a great day.\n")
             speak("Bye!. Have a great day.")
             exit()

         else:
             print("Sorry, I couldn't help you with this search. Please try something else!\n")
             speak("Sorry, I couldn't help you with this search. Please try something else!")


if __name__ == "__main__":
     main()
     