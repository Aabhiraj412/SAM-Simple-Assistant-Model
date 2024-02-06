import speech_recognition as sr
import os
import pyttsx3
import datetime
import webbrowser
import wikipedia
import cv2
import time
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def say(text):
    engine.say(text)
    print(text)
    engine.runAndWait()
    os.system('cls')

gflag = 0


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        say("Good Afternoon Sir")

    else:
        say("Good Evening Sir")

    
def command():
    global gflag
    if (gflag<3):
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print('Listening...')
            audio = r.listen(source)
            os.system('cls')
            print('Recognizing...')
            try:
                quary = r.recognize_google(audio)
                os.system('cls')
                gflag = 0
                return quary
            except Exception as e:
                gflag = gflag + 1
                os.system('cls')
                say('So Sorry Sir')
                say('But Seems liek some ERROR Occur')
                if gflag == 3:
                    say("Switching to Text input mode: ")
                say("Please try again")
                return "error"
    quary = input("Your Prompt: ")
    return quary
            

if __name__ == '__main__':
    os.system('cls')
    wish()
    say("I am S A M")
    say("SAM")
    say("Simple Assistant Model")
    say("How May I Help You")
    while True:
        flag = 0
        quary = command()
        if "sam" in quary.lower():
            quaru = quary.replace("sam", "SAM")
        print(quary)
        time.sleep(2)
        os.system('cls')
        greetings = [["hello ", "Hi"],
        ["hi ", "Hello"],
        ["good morning", "Good Morning"],
        ["good night", "Good Night"],
        ["good day", "Good Day"],
        ["good evening", "Good Evening"],
        ["hey ", "Hello"],
        ["hay ", "Hello"]]

        creators = ['programmer','father','creator','maker','owner']

        closes = ["quit"," exit"," end"," close"," finish"]

        savages = [["Fuck You", "Fuck You Too Sir"]]
        
        jokes =[["joke0","I Know a good one","Your Life"],
        ['joke1','Don’t you hate it when someone answers their own questions?','Well I do.'],
        ['joke2','I know they say that money talks','but all mine says is Goodbye.'],
        ['joke3','Most people are shocked when they find out how bad I am as an electrician.'],
        ['joke4','Never trust atoms','They make up everything.']]

        yous = ['tell me about yourself','tell me something about yourself', 'what are you', 'who are you']

        sites = [["youtube","YouTube", "http://www.youtube.com"],
        ["google","Google", "http://www.google.com"],
        ["wikipedia","Wikipedia", "https://www.wikipedia.org/"],
        ["stack overflow","Stack OverFlow", "http://www.stackoverflow.com"],
        ["Hackerrank","HackerRank", "http://www.www.hackerrank.com"],
        ["chat gpt","Chat GPT", "https://chat.openai.com/"],
        ["gmail","Gmail", "http://mail.google.com/mail/u/0/#inbox"],
        ["mail","Gmail", "http://mail.google.com/mail/u/0/#inbox"],
        ["instagram","Instagram", "http://www.ginstagram.com"],
        ["shop","Amazon", "http://www.amazon.in"],
        ["amazon","Amazon", "http://www.amazon.in"],
        ["Hotstar","Hotstar", "http://www.hotstar.com/in"],
        ["movies","Hotstar", "http://www.hotstar.com/in"],
        ["series","Hotstar", "http://www.hotstar.com/in"],
        ["chrome","Web Browser", "http://www.google.com"],
        ["brave","Web Browser", "http://www.google.com"],
        ["browser","Web Browser", "http://www.google.com"]]
        
        if (quary == "error"):
            continue

        for site in sites:
            if f"open {site[0]}".lower() in quary.lower():
                say(f"Opening {site[1]}")
                webbrowser.open(site[2])
                time.sleep(5)
                flag = 1
        
        for savage in savages:
            if (f"{savage[0]}".lower() in quary.lower()):
                say(f"{savage[1]}")
                flag = 1
        
        for close in closes:
            if f"{close}".lower() in quary.lower():
                say("Ok Sir")
                say("Have A Nice Day")
                say("SAM Signing Out")
                quit()

        for greeting in greetings:
            if f"{greeting[0]}" in quary:
                say(f'{greeting[1]} Sir.')
                if 'how are you' or 'how r u' in quary:
                    say('I am Fine')
                say(' How can i help you')
                time.sleep(2)
                flag = 1
                
        for you in yous:
            if you in quary:
                say("I am SAM")
                say("Simple Assistant Model")
                say('I am a simple desktop assistant programed by Mr Abhiraj Dixit to perform basic task on your pc')
                say("How May I Help You")
                flag = 1
                
        for creator in creators:
            if creator in quary:
                say(F'Mr Abhiraj Dixit can be recognised as my {creator}')
                say("How May I Help You")
                flag = 1

        if(flag == 1):
            continue

        if 'time' in quary.lower() and "mean" not in quary.lower() and "about" not in quary.lower():
            strTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Currently, the time is {strTime}")

        elif "voice input" in quary.lower() or ("flag" and "zero" in quary.lower()) :
            say ('Switching to Voice Input Mode')
            gflag = 0

        elif ("text input" in quary.lower()) or ("flag" and "three" in quary.lower()) :
            say ('Switching to Text Input Mode')
            gflag = 3

        elif 'how are you' in quary.lower() or 'how r u' in quary.lower():
            say('I am Fine')
            say('How Are You Sir')
            rep  = command()
            if  ("fine" or 'good' or 'great' in rep) and "not" in rep:
                say('oh')
                say('I see')
            elif "fine" or 'good' or 'great' in rep:
                say('Thats Great') 
            say("How can I help you")
            continue

        elif "joke" in quary.lower():
            r = random.randrange(0,len(jokes))
            st = f"joke{r}"
            for joke in jokes:
                if st == joke[0]:
                    say(joke[1])
                    time.sleep(1)
                    say(joke[2])

        elif "open camera" in quary:
            say("Opening Camera")
            say("Press ESC to exit...")
            cv2.namedWindow("Camera")
            vc = cv2.VideoCapture(0)

            if vc.isOpened():
                rval, frame = vc.read()
            else:
                rval = False

            while rval:
                cv2.imshow("Camera", frame)
                rval, frame = vc.read()
                key = cv2.waitKey(20)
                if key == 27: # exit on ESC
                    break
                
            vc.release()
            cv2.destroyWindow("Camera")

        elif ('what' in quary.lower()) or ("tell me" in quary.lower() and "more" not in quary.lower()) or ("describe" in quary.lower()):
            quary = quary.lower()
            quary = quary.replace("what ", "")
            quary = quary.replace("is ", "")
            quary = quary.replace("describe ", "")
            quary = quary.replace("tell me about ", "")
            quary = quary.replace("tell me something about ", "")
            quary = quary.replace("do you mean by ", "")
            say("Please Wait...")
            say(f"Gathering Information about {quary.upper()}")
            results = wikipedia.summary(quary, sentences=2)
            say("According to wikipedia ")
            say(results)

        elif "tell me more about" in quary.lower():
            quary = quary.replace("tell me more about ", "")
            say("Showing Results for "+quary+" on Google")
            quary = quary.replace(" ", "+")
            webbrowser.open(f'https://search.brave.com/search?q={quary}&source=desktop')
            time.sleep(5)

        elif "play music" in quary.lower():
            say('Playing Music')
            webbrowser.open('https://www.youtube.com/watch?v=3chGVpR9NzA&list=PLvdln1EiNh1yiBCVY_lIJLQcWYvyWIO5W&index=1')
        
        elif "play song" in quary.lower():
            say('Playing Music')
            webbrowser.open('https://www.youtube.com/watch?v=3chGVpR9NzA&list=PLvdln1EiNh1yiBCVY_lIJLQcWYvyWIO5W&index=1')

        elif 'play raps' in quary:
            say('Playing Raps')
            webbrowser.open('https://www.youtube.com/watch?v=lLBHqMZ92C4&list=PLvdln1EiNh1xpsaE0tDV4TFrt0XFsn1T0&index=1')


        elif "open" in quary.lower() and "youtube" not in quary.lower():
            quary = quary.replace("open " , "")
            say("opening "+quary)
            quary = quary.replace(" ", "+")
            webbrowser.open(f'https://search.brave.com/search?q={quary}&source=desktop')

        elif "open" in quary.lower() or "play" in quary.lower() and "youtube" in quary.lower():
            quary = quary.replace("play " , "")
            quary = quary.replace("open " , "")
            quary = quary.replace("YouTube" , "")
            quary = quary.replace("on", "")
            say(f"Opening {quary} on Youtube")

            quary = quary.replace(" ","+")
            webbrowser.open(f"https://www.youtube.com/results?search_query={quary}")
            time.sleep(5)

        
        elif "play" in quary.lower():
            quary = quary.replace("play " , "")
            quary = quary.replace(" ", "+")
            say(f"Opening {quary} on Youtube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={quary}")
            time.sleep(5)

        else:
            say(f"Sir, my apologies but i cant find result for: {quary} in existing database.")
            say("Googling the Result")
            quary = quary.replace(" ", "+")
            webbrowser.open(f'https://search.brave.com/search?q={quary}&source=desktop')
            time.sleep(5)
