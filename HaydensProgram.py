import tkinter as tk
import os
import webbrowser
from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import *


def open():
    os.startfile(r'notepad.exe')
def open2():
    os.startfile(r'code1.py')
def open3():
    os.startfile(r'calc')
def browser1():
    webbrowser.get('windows-default').open('www.google.ca')
def browser2():
    webbrowser.get('windows-default').open('https://www.ge-tracker.com/osrs-market-watch')
def getweather():
    city = "CAON4756:1:CA"
    webbrowser.get('windows-default').open('https://weather.com/en-CA/weather/today/l/'+city)
def duckduckgoose():
    webbrowser.get('windows-default').open('http://duckduckgo.com')
def facebook():
    webbrowser.get('windows-default').open('http://facebook.com')
def messenger():
    webbrowser.get('windows-default').open('https://www.facebook.com/messages/t/')
def youtube():
    webbrowser.get('windows-default').open('https://www.youtube.com')
def githhub():
    webbrowser.get('windows-default').open('https://github.com/darkerjedi98/runelitemultilauncher')
def whatsapp():
    webbrowser.get('windows-default').open('https://web.whatsapp.com/')


HEIGHT = 25
WIDTH = 270

root = tk.Tk()
root.title("Haydens's Launcher")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,)
canvas.pack()

background_image = tk.PhotoImage(file='~/Documents/image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)



button = tk.Button(root, text="notepad",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=7, command=open)

button.pack(fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="calc",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=10, command=open3)

button.pack(fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="google",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=browser1)
button.pack(fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="ge tracker",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=browser2)
button.pack(side='left',pady = 10, padx = 10)

button = tk.Button(root, text="get weather",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=getweather)
button.pack(side='left',pady = 10, padx = 10)

button = tk.Button(root, text="duckduckgo",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=duckduckgoose)
button.pack(side='left',pady = 10, padx = 10)

button = tk.Button(root, text="facebook",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=facebook)
button.pack(side='left',pady = 10, padx = 10)

button = tk.Button(root, text="messenger",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=messenger)
button.pack(side='left',pady = 10, padx = 10)

button = tk.Button(root, text="youtube",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=youtube)
button.pack(side='left',pady = 10, padx = 10)

button = tk.Button(root, text="githhub",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=githhub)
button.pack(fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="whatsapp",font=('Helvetica', '10'), bg='green', fg='black', height=3, width=17, command=whatsapp)
button.pack(fill = BOTH, expand = True,pady = 10, padx = 10)

root.mainloop()