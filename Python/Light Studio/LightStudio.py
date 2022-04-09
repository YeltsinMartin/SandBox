from ast import walk
from msilib.schema import ListBox
from tkinter import *
import tkinter as tk
import os
from tkinter import colorchooser
from turtle import left
from pygame import mixer

time = 0
colorData = []
hatColour = []
shirtColour = []
pantColour = []
gloveColour = []
shoeColour = []

'''
def hatColorPciker():
    global hatColour
    hatColour, color = colorchooser.askcolor()
    hatLabel.config(bg=color)
    root.update()

def shirtColorPciker():
    global shirtColour
    shirtColour, color = colorchooser.askcolor()
    shirtLabel.config(bg=color)
    root.update()

def pantColorPciker():
    global pantColour
    pantColour, color = colorchooser.askcolor()
    pantLabel.config(bg=color)
    root.update()

def gloveColorPciker():
    global gloveColour
    gloveColour, color = colorchooser.askcolor()
    gloveLabel.config(bg=color)
    root.update()
    
def shoeColorPciker():
    global shoeColour
    shoeColour, color = colorchooser.askcolor()
    shoeLabel.config(bg=color)
    root.update()

def saveTime():
    global time
    data = []
    data.append(hatColour)
    data.append(shirtColour)
    data.append(pantColour)
    data.append(gloveColour)
    data.append(shoeColour)
    colorData.append(data)
    time = time + 1
    timeLabel.config(text="TIME: {0} seconds".format(time))
    root.update()
    print(data)

def saveData():
    with open("out.txt", "w") as file:
        for data in colorData:
            file.write(str(data)+ "\n")


root = Tk()
root.title("Light Studio")
root.geometry("400x400")

hatLabel = Label(root, text="Hat Colour")
hatButton = Button(root, text = "Choose hat Colour", command = hatColorPciker)


shirtLabel = Label(root, text="shirt Colour")
shirtButton = Button(root, text = "Choose shirt Colour", command = shirtColorPciker)


pantLabel = Label(root, text="pant Colour")
pantButton = Button(root, text = "Choose pant Colour", command = pantColorPciker)


gloveLabel = Label(root, text="glove Colour")
gloveButton = Button(root, text = "Choose glove Colour", command = gloveColorPciker)


shoeLabel = Label(root, text="shoe Colour")
shoeButton = Button(root, text = "Choose shoe Colour", command = shoeColorPciker)

timeLabel = Label(root, text="TIME: {0} seconds".format(time))
timeButton = Button(root, text = "Next Frame", command = saveTime)

saveButton = Button(root, text = "Save Data", command = saveData)

hatLabel.pack()
hatButton.pack()
shirtLabel.pack()
shirtButton.pack()
pantLabel.pack()
pantButton.pack()
gloveLabel.pack()
gloveButton.pack()
shoeLabel.pack()
shoeButton.pack()
timeLabel.pack()
timeButton.pack()
saveButton.pack()

root.mainloop()
'''

mp3Files = []
datFiles = []

playing = False
def hatColorPciker():
    hatColour, color = colorchooser.askcolor()
    f1b1.config(bg=color)
    canvas.update()

def shirtColorPciker():
    shirtColour, color = colorchooser.askcolor()
    f1b2.config(bg=color)
    canvas.update()

def pantColorPciker():
    pantColour, color = colorchooser.askcolor()
    f1b3.config(bg=color)
    canvas.update()

def gloveColorPciker():
    gloveColour, color = colorchooser.askcolor()
    f1b4.config(bg=color)
    canvas.update()
    
def shoeColorPciker():
    shoeColour, color = colorchooser.askcolor()
    f1b5.config(bg=color)
    canvas.update()

def playCmd() -> None:
    global playing
    if not playing:
        songLabel.config(text= songBox.get("anchor"))
        mixer.music.load(os.getcwd()+"\\"+songBox.get("anchor"))
        mixer.music.play()
        playing = True
    else:
        mixer.music.unpause()

def pauseCmd() -> None:
    mixer.music.pause()

def stopCmd() -> None:
    global playing
    mixer.music.stop()
    songLabel.config(text="")
    songBox.select_clear('active')
    playing= False

for r, fo, fi in os.walk(os.getcwd()):
    mp3Files = [file for file in fi  if file.find(".mp3") != -1]
    datFiles = [file for file in fi  if file.find(".dat") != -1]

canvas = Tk()
canvas.title("Light Studio")
canvas.geometry("800x600")
canvas.config(bg='black')

mixer.init()

playImg = PhotoImage(file="play.png")
pauseImg = PhotoImage(file="pause.png")
stopImg = PhotoImage(file="stop.png")
capImg =  PhotoImage(file="cap.png")
shirtImg =  PhotoImage(file="shirt.png")
shoeImg =  PhotoImage(file="shoe.png")
gloveImg =  PhotoImage(file="glove.png")
pantImg =  PhotoImage(file="pant.png")

f0 = tk.Frame(canvas,padx=10, pady=10,bg= "black")
f1 = tk.Frame(canvas,padx=10, pady=10,bg= "black")
f2 = tk.Frame(canvas,padx=10, pady=10,bg= "black")
f3 = tk.Frame(canvas,padx=10, pady=10,bg= "black")
f4 = tk.Frame(canvas,padx=10, pady=10,bg= "black")
f5 = tk.Frame(canvas,padx=10, pady=10,bg= "black")
f6 = tk.Frame(canvas,padx=10, pady=10,bg= "black")

f0.grid(row=0,column=0, sticky="nsew")
f1.grid(row=0,column=1, sticky="nsew")
f2.grid(row=0,column=2, sticky="nsew")
f3.grid(row=0,column=3, sticky="nsew")
f4.grid(row=0,column=4, sticky="nsew")
f5.grid(row=0,column=5, sticky="nsew")
f6.grid(row=1, sticky="nsew")

#try anchor
songBox = Listbox(f0, fg = "green", bg ="black", width=50)
songBox.pack(padx=10, pady=10)

datBox = Listbox(f0, fg = "cyan", bg ="black", width=50)
datBox.pack(padx=10, pady=10)

songLabel = Label(f6, text="", fg = "yellow", bg ="black")
songLabel.pack()


## 5 person
f1b1 = tk.Button(f1, text="h",image=capImg, bg = "black", borderwidth=0, command=hatColorPciker)
f1b2 = tk.Button(f1, text="s",image=shirtImg, bg = "black", borderwidth=0, command=shirtColorPciker)
f1b3 = tk.Button(f1, text="p",image=pantImg, bg = "black", borderwidth=0, command=pantColorPciker)
f1b4 = tk.Button(f1, text="g",image=gloveImg, bg = "black", borderwidth=0, command=gloveColorPciker)
f1b5 = tk.Button(f1, text="s",image=shoeImg, bg = "black", borderwidth=0, command=shoeColorPciker)

f2b1 = tk.Button(f2, text="h",image=capImg, bg = "black", borderwidth=0)
f2b2 = tk.Button(f2, text="s",image=shirtImg, bg = "black", borderwidth=0)
f2b3 = tk.Button(f2, text="p",image=pantImg, bg = "black", borderwidth=0)
f2b4 = tk.Button(f2, text="g",image=gloveImg, bg = "black", borderwidth=0)
f2b5 = tk.Button(f2, text="s",image=shoeImg, bg = "black", borderwidth=0)

f3b1 = tk.Button(f3, text="h",image=capImg, bg = "black", borderwidth=0)
f3b2 = tk.Button(f3, text="s",image=shirtImg, bg = "black", borderwidth=0)
f3b3 = tk.Button(f3, text="p",image=pantImg, bg = "black", borderwidth=0)
f3b4 = tk.Button(f3, text="g",image=gloveImg, bg = "black", borderwidth=0)
f3b5 = tk.Button(f3, text="s",image=shoeImg, bg = "black", borderwidth=0)

f4b1 = tk.Button(f4, text="h",image=capImg, bg = "black", borderwidth=0)
f4b2 = tk.Button(f4, text="s",image=shirtImg, bg = "black", borderwidth=0)
f4b3 = tk.Button(f4, text="p",image=pantImg, bg = "black", borderwidth=0)
f4b4 = tk.Button(f4, text="g",image=gloveImg, bg = "black", borderwidth=0)
f4b5 = tk.Button(f4, text="s",image=shoeImg, bg = "black", borderwidth=0)

f5b1 = tk.Button(f5, text="h",image=capImg, bg = "black", borderwidth=0)
f5b2 = tk.Button(f5, text="s",image=shirtImg, bg = "black", borderwidth=0)
f5b3 = tk.Button(f5, text="p",image=pantImg, bg = "black", borderwidth=0)
f5b4 = tk.Button(f5, text="g",image=gloveImg, bg = "black", borderwidth=0)
f5b5 = tk.Button(f5, text="s",image=shoeImg, bg = "black", borderwidth=0)

playButton = Button(f6, text = "Play", command=playCmd, image=playImg, bg = "black", borderwidth=0)
pauseButton = Button(f6, text = "Pause", command=pauseCmd, image=pauseImg, bg = "black", borderwidth=0)
stopButton = Button(f6, text = "Stop", command=stopCmd, image=stopImg, bg = "black", borderwidth=0)

playButton.pack(padx=10, side="left")
pauseButton.pack(padx=10, side="left")
stopButton.pack(padx=10, side="left")

f1b1.pack()
f1b2.pack()
f1b3.pack()
f1b4.pack()
f1b5.pack()

f2b1.pack()
f2b2.pack()
f2b3.pack()
f2b4.pack()
f2b5.pack()

f3b1.pack()
f3b2.pack()
f3b3.pack()
f3b4.pack()
f3b5.pack()

f4b1.pack()
f4b2.pack()
f4b3.pack()
f4b4.pack()
f4b5.pack()

f5b1.pack()
f5b2.pack()
f5b3.pack()
f5b4.pack()
f5b5.pack()

for song in mp3Files:
    songBox.insert('end', song)

for dat in datFiles:
    datBox.insert('end', dat)

canvas.mainloop()
mixer.quit()