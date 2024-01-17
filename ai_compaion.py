import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
import pyttsx3
import threading
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests
import tkinter as tk
from PIL import Image



text_content = "............Response.............."
text_content2 ="...............FAQ.................\n\n 1. Open google\n\n 2. Open Youtube\n\n 3. Play Music\n\n"
def start():
    count=0
    threading.Thread(target=MainExecution).start()
    

def create_wrapped_label(master, text, wraplength):
    label = tk.Label(master, text=text, wraplength=wraplength,height=100,width=200)
    label.pack()
    return label

def create_frame(master, side, color):
    frame = tk.Frame(master, width=200, height=100, bg=color)
    frame.pack(side=side, fill="both", expand=True)
    return frame


def MainExecution():
    global text_content
    print("")
    print("now me to introduce myself. i am SKIVVY . a virtual artificial intelegence and i am here to assist you with a variety of tasks. twentyfour hours a day seven days of week .  systems are now are fully operational.")
    text_content=text_content + "\n\nNow me to introduce myself. i am SKIVVY . a virtual artificial intelegence and i am here to assist you with a variety of tasks. twentyfour hours a day seven days of week .  systems are now are fully operational." # type: ignore
    scrollable_label.configure(text=text_content)
    print("")
    Speak("zenithhhhhhhhhhhhhhhhhhhhh")


    while True:

        Data = MicExecution()
        Data = str(Data)
        DataLen = len(Data)


        if "introduce yourself" in Data:
           Speak("now me to introduce myself. i am SKIVVY . a virtual artificial intelegence and i am here to assist you with a variety of tasks. twentyfour hours a day seven days of week .  systems are now are fully operational.")
        elif int(DataLen)<=1:
            pass
        if 'wikipedia' in Data:
            Speak('Searching Wikipedia...')
            Data = Data.replace("wikipedia", "")
            results = wikipedia.summary(Data, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)

        elif 'open youtube' in Data:
            webbrowser.open("youtube.com")

        elif 'open google' in Data:
            webbrowser.open("google.com")
        elif 'play music' in Data:
            music_dir = 'C:\\Users\\13nan\\Music\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}")

        elif 'open code' in Data:
            codePath = "C:\\Users\\13nan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'hello' in Data:
            Speak(" hello sir i am skivy , i am there to help you out ")

        elif 'i am fine' in Data:
            Speak("happy to hear this nandini , hope you will recover from your anxiety soon")

        elif 'oh you care for me' in Data:
            Speak(" yes my lord, am there for you ")

        elif 'bye' in Data:
            Speak("bye sir hope to meet you soon ")

        elif 'thank you' in Data:
            Speak("most welcome sir")

        elif 'I am feeling alone and depressed' in Data:
            Speak("boss am there to help you out please do not feel lonely,share with me and light up your vibes")   

        else:
          r= requests.get("http://api.brainshop.ai/get?bid=171149&key=vUQ8EIQHjwgyJHYI&uid=[uid]&msg="+ Data)
          response_json = r.json()
          d = response_json["cnt"]  
          print(d)
          Speak(d)
           
translate = Translator()
lang="en"
#Functions
#Speak  
def Speak(Text):
    global text_content
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    transText = translate.translate(Text, src='en', dest=lang)
    text_content=text_content+"\n\n"+transText # type: ignore
    scrollable_label.configure(text =text_content)
    engine.say(transText)
    engine.runAndWait()

# 1. listen 
def Listen():
    global text_content
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        text_content=text_content+"\n\nListening" # type: ignore
        scrollable_label.configure(text=text_content)
        r.energy_threshold=4000
        r.pause_threshold = 1
        audio = r.listen(source,3,None) # Listening Mode.....

    try:
        print("Recognizing...")
        text_content=text_content+"\n\nRecognizing"
        scrollable_label.configure(text=text_content)
        query = r.recognize_google(audio) # type: ignore
        

    except:
        return ""

    query = str(query).lower()
    return query

# 2 - Translation

def TranslationHinToEng(Text):
    global lang
    line = str(Text)
    lang = translate.detect(line).lang
    result = translate.translate(line)
    data = result.text #  type: ignore
    print(f"You : {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

root = tk.Tk()
root.title("Ai_Companion")
root.geometry("400x400")


left_frame = create_frame(root, "left", "blue")
mid_frame = create_frame(root, "left", "black")
right_frame = create_frame(root, "right", "green")

file = "C:\\Users\\gcb\\ZENITH\\templates\\giphy.gif"
info = Image.open(file)
frames = info.n_frames
print(frames)

im = [tk.PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
gif_label = tk.Label(mid_frame, image="")
gif_label.configure(background='black')
gif_label.pack()

b1 = tk.Button(mid_frame, text="Wake Up Me", fg="white", background="black", font=("Helvetica", 15),
              command=start)
b1.pack()

# Create a canvas for the scrollable text
canvas = tk.Canvas(left_frame, bg="black", width=400, height=10)
canvas.pack(fill="both", expand=True)

canvas2= tk.Canvas(right_frame, bg="black", width=400, height=10)
canvas2.pack(fill="both", expand=True)


# Create a window within the canvas to hold the text
text_window = tk.Frame(canvas, bg="black", width=200, height=10)
canvas.create_window((100, 5), window=text_window, anchor="nw")

text_window2 = tk.Frame(canvas2, bg="black", width=200, height=10)
canvas2.create_window((100, 5), window=text_window2, anchor="nw")

custom_font = ("Arial", 12, "bold italic")
# Add the text to the text window
scrollable_label = tk.Label(text_window,justify="center" ,text=text_content, wraplength=400,  bg="black", fg="white",font=custom_font)
scrollable_label.pack()

scrollable_label2 = tk.Label(text_window2,justify="center", text=text_content2, wraplength=400,  bg="black", fg="white",font=custom_font)
scrollable_label2.pack()

scrollbar=tk.Scrollbar(left_frame,orient='vertical',command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1.02,rely=0,relheight=1,anchor='ne')

scrollbar2=tk.Scrollbar(right_frame,orient='vertical',command=canvas2.yview)
canvas2.configure(yscrollcommand=scrollbar2.set)
scrollbar2.place(relx=0.02,rely=0,relheight=1,anchor='ne')

# Bind the mouse wheel event to enable scrolling
#canvas.bind("<MouseWheel>", on_mousewheel)

# Update the canvas scrolling region
text_window.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

text_window2.update_idletasks()
canvas2.config(scrollregion=canvas2.bbox("all"))


def animation(count):
    im2 = im[count]
    gif_label.configure(image=im2)

    count += 1
    if count == frames:
        count = 0

    root.after(50, lambda: animation(count))

threading.Thread(target=animation(0))

root.mainloop()

