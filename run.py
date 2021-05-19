from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import wikipedia
import smtplib


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Evening, Prajwal Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Prajwal Sir")
    else:
        speak("Good Evening, Prajwal Sir")
        
    speak("Im your personal assistant, Tron. Please tell me how may I help you.")
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        # number of seconds once the phrase is considered complete
        # r.pause_threshold = 1
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
    server.login('prajwaltomar11@gmail.com', 'your password')
    server.sendmail('prajwaltomar11@gmail.com', to, content)
    server.close()

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        # while True:
        #     self.query = self.STT()
        #     if 'good bye' in self.query:
        #         sys.exit()
        #     elif 'open google' in self.query:
        #         webbrowser.open('www.google.co.in')
        #         speak("opening google")
        #     elif 'open youtube' in self.query:
        #         webbrowser.open("www.youtube.com")
        #     elif 'play music' in self.query:
        #         speak("playing music from pc")
        #         self.music_dir ="./music"
        #         self.musics = os.listdir(self.music_dir)
        #         os.startfile(os.path.join(self.music_dir,self.musics[0]))
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
                    speak("Sorry Prajwal sir. I am not able to send this email")

            elif 'how are you' in query:
                speak("I'm really good, Prajwal! Thank you for asking")

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











FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1680,900)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.jpg"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())