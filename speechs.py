import pyttsx3
import speech_recognition as sr
import psutil
import wikipedia
import datetime
import os, platform
import webbrowser
import subprocess
import winshell
import ctypes
import wikiquote
import pyjokes
from time import ctime
import smtplib

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")



r=sr.Recognizer()

def takeCommand(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
            speak(ask)

        r.pause_threshold=1
        audio=r.listen(source)
        query=""
    try:
        query=r.recognize_google(audio, language='en-in')
        print(f'user said:{query}')
    except ValueError:
        print("please check your connection")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return 'None'
    return query


if __name__=="__main__":
    wish()
    speak("do you need a quote of the day?")
    user_wish=takeCommand().lower()

    if 'yes' or 'sure' or 'ok' in user_wish:
        print(wikiquote.quote_of_the_day())
        speak(wikiquote.quote_of_the_day())
    else:
        speak("at ur convinience")

    speak("AT your service sir,  how can i help you")

    while True:
        query=takeCommand().lower()


        if 'what is your name' in query:
            print("I am Anu")
            speak("I am Anu")

        elif 'who are you' in query:
            print("I am Anu, your virtual assistant")
            speak("I am Anu, your virtual assistant")


        elif 'who created you' in query:
            print('stark created me')
            speak('stark created me')

        elif 'your favourite food' in query:
            print('i dont eat food,i take charge')
            speak('i dont ear food, i take charge')

        elif 'clean bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak('successful')

        elif 'shutdown' in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(4)
            subprocess.call('shutdown /p /f')

        elif 'lock screen' in query:
            ctypes.windll.user32.LockWorkStation()

        elif 'who am i' in query:
            print('you are a human')
            speak('you are a human')

        elif "why you came to world" in query:
            speak("It's a secret")

        elif 'how are you' in query:
            battery = psutil.sensors_battery()
            percent = str(battery.percent)
            if percent >=75:
                speak('healthy')
            elif percent >=40:
                speak('feeling good')
            elif percent<=40:
                sepak('not good, required charge')

        elif 'jokes' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'what time is it' in query:
            speak(ctime())
            print(ctime())

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'send email' in query:
            def sendEmail(to, content):
                server = smtplib.SMTP('smtp.gmail.com', 587)  # starts, gmail.com and port number in smtp
                server.ehlo()  # establish local host
                server.starttls()  # starts web and runs on web
                server.login('gopi80211@gmail.com', '')  # emial id and password
                server.sendmail('gopi80211@gmail.com', to, content)
                server.close()
            try:
                content = "HI"
                to = "ksharish3998@gmail.com"
                sendEmail(to, content)
                print("Email has been send")
            except Exception as e:
                print(e)
                print(f"Sorry sir, email not been sent to {to}")

        elif 'system info' in query:
            print(f'cpu count {os.cpu_count()}')
            print(f'platform info {platform.system()}')
            print(f"Machine: {platform.machine()}")
            print(f"Node Name: {platform.node()}")
            print(f"Release: {platform.release()}")
            print(f"Version: {platform.version()}")
            print(f"Processor: {platform.processor()}")

        elif 'your favourite color' in query:
            print('black')
            speak('black')

        elif 'show ram' in query:
            memoryUse = psutil.virtual_memory()[0] / 2. ** 30
            print('memory use:', memoryUse)

        elif 'status' in query:
            battery=psutil.sensors_battery()
            percent=str(battery.percent)
            print(f'Battery status is {percent} percent')
            speak(f'Battery status is {percent} percent')

        elif 'brightness' in query:
            br = wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0]
            br.WmiSetBrightness(100, 100)

        elif 'disk usage' in query:
            usage=takeCommand("which disk should i show usage")
            Disk = psutil.disk_usage(f'{usage}:\\')

            print(Disk.total / (1024.0 ** 3))
            print(Disk.used / (1024.0 ** 3))
            print(Disk.free / (1024.0 ** 3))
            print(Disk.percent)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'search' in query:
            search = takeCommand("what do you want to search for?")
            url = 'https://google.com/search?q=' + search
            webbrowser.open(url)
            speak("here is what i found for " + search)

        elif 'find location' in query:
            location = takeCommand("what do you want to search for?")
            url = 'https://google.nl/maps/place/' + location
            webbrowser.get().open(url)
            speak("here is what i found for " + location)

        elif "write a note" in query:
            note = takeCommand("what should i wrtie sir")
            file = open('anu.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("anu.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'open google' in query:
            speak("opening google for you")
            webbrowser.open("www.google.com")

        elif 'open youtube' in query:
            speak("opening youtube for you")
            webbrowser.open("www.youtube.com")

        elif 'songs' in query:
            songs=user_choice("which song i need to play?")
            for play in os.listdir("D:\\music"):
                if songs in play:
                    os.startfile(os.path.join(song, play))
                else:
                    url = 'https://youtube.com/results?/search?q=' + songs
                    webbrowser.get().open(url)
                    speak("here is what i found for " + song)

        elif 'open word' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk')

        elif 'open powerpoint' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007.lnk')

        elif 'open excel' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk')

        elif 'help' in query:
            print('''here is the list of commands that i can perform
            what is your name
            songs
            open word
            open excel
            open powerpoint
            help
            quit
            open google
            open youtube
            search
            wikipedia
            your favorite food
            your favorite color
            who created you
            who am i
            disk usage
            find location
            shutdown
            lockscreen
            brightness
            status
            show ram
            system info
            jokes
            note
            how are you
            send email
            ''')
            speak('''here is the list of commands that i can perform
                        what is your name
                        songs
                        open word
                        open excel
                        open powerpoint
                        help
                        quit
                        open google
                        open youtube
                        search
                        wikipedia
                        your favorite food
                        your favorite color
                        who created you
                        who am i
                        disk usage
                        find location
                        shutdown
                        lockscreen
                        brightness
                        status
                        show ram
                        system info
                        jokes
                        note
                        how are you
                        send email
                        ''')

        elif 'quit' in query:
            exit()