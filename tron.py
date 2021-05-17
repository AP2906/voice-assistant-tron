import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os


# setting up pyttsx3 by creating an instance called engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Prajwal!")

    elif hour >= 12 and hour < 18:
        speak("Good Morning, Prajwal!")

    else:
        speak("Good Morning, Prajwal!")

    speak("Im your personal assistant, Tron. Please tell me how may I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # number of seconds once the phrase is considered complete
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            # converts our audio into string using recognizer
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prajwaltomar11@gmail.com', 'Demonskull@26')
    server.sendmail('prajwaltomar11@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    quitbot = ""
    while quitbot != "exit":
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching the wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
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

        elif 'email to prajwal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prajwalstomar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my prajwal sir. I am not able to send this email")

        elif 'how are you' in query:
            speak("I'm really good, prajwal! after all im the assistant of the sexiest man alive and sherry is potty")

        elif 'your name' in query:
            speak("My Name is Tron!")

        elif 'exit' in query:
            speak("Bye Prajwal see you soon!")
            quitbot = "exit"

        elif 'open code' in query:
            codePath = "C:\\Users\\prajw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'sherry' in query:
            speak("sherry is a good girl")