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
def open4():
    os.startfile(r'RuneLite.exe')
def open5():
    os.startfile(r'RuneLite.exe')
    os.startfile(r'RuneLite.exe')
def launchcode():
    coin = (int(input('coins spent:')))
    rune = (int(input('nature rune cost:')))
    item = (int(input('# of items bought:')))
    price = (int(input('price per item:')))
    back = (int(input('money back(after selling):')))
    print(rune * item - coin - price + back)
    (print("profit:"))
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
def githhub1():
    webbrowser.get('windows-default').open('https://github.com/darkerjedi98/runelitemultilauncher')
def whatsapp():
    webbrowser.get('windows-default').open('https://web.whatsapp.com/')
def date1():
    os.startfile(r'outlookcal:')
def camera1():
    os.startfile(r'microsoft.windows.camera:')
def searchwiki():
    webbrowser.get('windows-default').open('https://oldschool.runescape.wiki/w/'+entry1.get())


HEIGHT = 25
WIDTH = 270

root = tk.Tk()
root.title("Darkerjedi's Launcher")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,)
canvas.pack()

background_image = tk.PhotoImage(file='./gif/image.png')
background_label = tk.Label(root, image=background_image, bg="#5F9EA0")
background_label.place(relwidth=1, relheight=1)

entry1 = tk.Entry (root) 
canvas.create_window(140, 20, window=entry1)

button = tk.Button(root, text="search OSRS WIKI",bg="black",font=('Helvetica', '10'),height=50, width=225, command=searchwiki)
wikisearch = PhotoImage(file="./gif/search.gif")
button.config(image=wikisearch)
button.pack(fill = Y, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="camera",bg="black",font=('Helvetica', '10'),height=125, width=175, command=camera1,)
img33 = PhotoImage(file="./gif/camera.gif")
button.config(image=img33)
button.pack(expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="classic",bg="black",font=('Helvetica', '10'),height=40, width=400, command=open2)
img3 = PhotoImage(file="./gif/classic.gif")
button.config(image=img3)
button.pack(fill =Y, expand = True,pady = 10, padx = 10)



button = tk.Button(root, text="Runelite",font=('Helvetica', '10'), bg='black', height=40, width=320, command=open4)
img6 = PhotoImage(file="./gif/runelite.gif")
button.config(image=img6)
button.pack(fill =Y, expand = True,pady = 10, padx = 10)


button = tk.Button(root, text="notepad",font=('Helvetica', '10'), bg='black', height=40, width=320, command=open)
img8 = PhotoImage(file="./gif/notepad.gif")
button.config(image=img8)
button.pack(fill =Y, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="calc",font=('Helvetica', '10'), bg='black', height=40, width=320, command=open3)
img9 = PhotoImage(file="./gif/calculator.gif")
button.config(image=img9)
button.pack(fill =Y, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="launch 2 runelite's",font=('Helvetica', '10'), bg='black', height=40, width=320, command=open5)
img10 = PhotoImage(file="./gif/launch2runelite.gif")
button.config(image=img10)
button.pack(fill =Y, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="profit calc",font=('Helvetica', '10'), bg='black', height=40, width=320, command=launchcode)
img11 = PhotoImage(file="./gif/profitcalc.gif")
button.config(image=img11)
button.pack(fill =Y, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="google",font=('Helvetica', '10'), bg='black', height=35, width=320, command=browser1)
img12 = PhotoImage(file="./gif/google.gif")
button.config(image=img12)
button.pack(fill =Y, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="ge tracker",font=('Helvetica', '10'), bg='black', height=3, width=155, command=browser2)
img17 = PhotoImage(file="./gif/ge_tracker.gif")
button.config(image=img17)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="get weather",font=('Helvetica', '10'), bg='black', height=3, width=160, command=getweather)
img16 = PhotoImage(file="./gif/get_weather.gif")
button.config(image=img16)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="duckduckgo",font=('Helvetica', '10'), bg='black', height=3, width=175, command=duckduckgoose)
img15 = PhotoImage(file="./gif/duckduckgo.gif")
button.config(image=img15)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="facebook",font=('Helvetica', '10'), bg='black', height=3, width=150, command=facebook)
img14 = PhotoImage(file="./gif/facebook.gif")
button.config(image=img14)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="messenger",font=('Helvetica', '10'), bg='black', height=3, width=175, command=messenger)
img13 = PhotoImage(file="./gif/messenger.gif")
button.config(image=img13)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="youtube",font=('Helvetica', '10'), bg='black', height=3, width=150, command=youtube)
img7 = PhotoImage(file="./gif/youtube.gif")
button.config(image=img7)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="date",font=('Helvetica', '10'), bg='black', height=3, width=100, command=date1)
img5 = PhotoImage(file="./gif/date1.gif")
button.config(image=img5)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="githhubb",bg="black",font=('Helvetica', '10'),height=50, width=100, command=githhub1)
img1 = PhotoImage(file="./gif/githhub.gif")
button.config(image=img1)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

button = tk.Button(root, text="whatsapp",bg="black",font=('Helvetica', '10'),height=50, width=140, command=whatsapp)
img = PhotoImage(file="./gif/whatsapp.gif")
button.config(image=img)
button.pack(side='left',fill = BOTH, expand = True,pady = 10, padx = 10)

root.mainloop()