import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser




engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good moring")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello khushal!, i am jaara , how may  i help you ")  

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        # print(e)
        print("Say that agian please")
        return "none"
    return query    

if __name__ == "__main__":
   wishme()
   while True:
    query= takecommand().lower()

   #logic for executing task , based on query
    if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com")    

    elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")                