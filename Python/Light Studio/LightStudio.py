from abc import abstractmethod, abstractstaticmethod
from ast import List
import tkinter as tk
import os
from pygame import mixer
from tkinter import colorchooser
time = 0
colorData = []

class IPerson:
    
    @abstractmethod
    def getData(self) -> list:
        """implemented in person"""
class Person(IPerson):
    canvas = None

    def __init__(self,frame) -> None:
        self.capColour = [0,0,0]
        self.shirtColour = [0,0,0]
        self.pantColour = [0,0,0]
        self.gloveColour = [0,0,0]
        self.shoeColour = [0,0,0]
        self.capKey   = '#000000'
        self.shirtKey = '#000000'
        self.pantKey  = '#000000'
        self.gloveKey = '#000000'
        self.shoeKey  = '#000000'

        self.capImg   =  tk.PhotoImage(file="cap.png")
        self.shirtImg =  tk.PhotoImage(file="shirt.png")
        self.shoeImg  =  tk.PhotoImage(file="shoe.png")
        self.gloveImg =  tk.PhotoImage(file="glove.png")
        self.pantImg  =  tk.PhotoImage(file="pant.png")

        self.capButton   = tk.Button(frame, text="h",image=self.capImg, bg = "black", borderwidth=0,   command=self.capColorPciker)
        self.shirtButton = tk.Button(frame, text="s",image=self.shirtImg, bg = "black", borderwidth=0, command=self.shirtColorPciker)
        self.pantButton  = tk.Button(frame, text="p",image=self.pantImg, bg = "black", borderwidth=0,  command=self.pantColorPciker)
        self.gloveButton = tk.Button(frame, text="g",image=self.gloveImg, bg = "black", borderwidth=0, command=self.gloveColorPciker)
        self.shoeButton  = tk.Button(frame, text="s",image=self.shoeImg, bg = "black", borderwidth=0,  command=self.shoeColorPciker)

        self.capButton.pack()   
        self.shirtButton.pack()
        self.pantButton.pack()
        self.gloveButton.pack()
        self.shoeButton.pack()

    def capColorPciker(self) -> None:
        self.capColour, self.capKey = colorchooser.askcolor()
        self.capButton.config(bg=self.capKey)
        Person.canvas.update()

    def shirtColorPciker(self) -> None:
        self.shirtColour, self.shirtKey = colorchooser.askcolor()
        self.shirtButton.config(bg=self.shirtKey)
        Person.canvas.update()

    def pantColorPciker(self) -> None:
        self.pantColour, self.pantKey = colorchooser.askcolor()
        self.pantButton.config(bg=self.pantKey)
        Person.canvas.update()

    def gloveColorPciker(self) -> None:
        self.gloveColour, self.gloveKey = colorchooser.askcolor()
        self.gloveButton.config(bg=self.gloveKey)
        Person.canvas.update()
        
    def shoeColorPciker(self) -> None:
        self.shoeColour, self.shoeKey = colorchooser.askcolor()
        self.shoeButton.config(bg=self.shoeKey)
        Person.canvas.update()

    def getData(self) -> list:
        colorList = []
        colorList.append({self.capKey:self.capColour})
        colorList.append({self.shirtKey:self.shirtColour})
        colorList.append({self.pantKey:self.pantColour})
        colorList.append({ self.gloveKey:self.gloveColour})
        colorList.append({self.shoeKey:self.shoeColour})
        return colorList

'''
def capColorPciker():
    global capColour
    capColour, color = colorchooser.askcolor()
    capLabel.config(bg=color)
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
    data.append(capColour)
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

capLabel = Label(root, text="cap Colour")
capButton = Button(root, text = "Choose cap Colour", command = capColorPciker)


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

capLabel.pack()
capButton.pack()
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

def saveTime():
    global time
    time += 1
    data = []
    for person in persons:
        data.append(person.getData())
    #print(data) ##commented for debugging
    colorData.append(data)
    timeLabel.config(text="TIME: {0} seconds".format(time))
    canvas.update()

def saveData():
    with open("out.dat", "w") as file:
        for data in colorData:
            file.write(str(data)+ "\n")

def simCmd() -> None:
    pass

for r, fo, fi in os.walk(os.getcwd()):
    mp3Files = [file for file in fi  if file.find(".mp3") != -1]
    datFiles = [file for file in fi  if file.find(".dat") != -1]

canvas = tk.Tk()
canvas.title("Light Studio")
canvas.geometry("800x600")
canvas.config(bg='black')

mixer.init()

playImg  = tk.PhotoImage(file="play.png")
pauseImg = tk.PhotoImage(file="pause.png")
stopImg  = tk.PhotoImage(file="stop.png")
simImg   = tk.PhotoImage(file="sim.png")
saveImg  = tk.PhotoImage(file="save.png")
nextImg  = tk.PhotoImage(file="next.png")

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
f6.grid(row=1,columnspan=6, sticky="nsew")

#try anchor
songBox = tk.Listbox(f0, fg = "green", bg ="black", width=50)
songBox.pack(padx=10, pady=10)

datBox = tk.Listbox(f0, fg = "cyan", bg ="black", width=50)
datBox.pack(padx=10, pady=10)

songLabel = tk.Label(f6, text="", fg = "yellow", bg ="black")
songLabel.pack()

timeLabel  = tk.Label(f6, text="TIME: {0} seconds".format(time), bg="black", fg="cyan", borderwidth=0)
nextButton = tk.Button(f6, text = "Next Frame", command = saveTime, image=nextImg, bg="black", fg="white", borderwidth=0)
saveButton = tk.Button(f6, text = "Save Data" , command = saveData, image=saveImg, bg="black", fg="white", borderwidth=0)
simButton  = tk.Button(f6, text = "Play"      , command = simCmd, image=simImg, bg = "black", fg="white", borderwidth=0)

playButton  = tk.Button(f6, text = "Play", command=playCmd, image=playImg, bg = "black", borderwidth=0)
pauseButton = tk.Button(f6, text = "Pause", command=pauseCmd, image=pauseImg, bg = "black", borderwidth=0)
stopButton  = tk.Button(f6, text = "Stop", command=stopCmd, image=stopImg, bg = "black", borderwidth=0)

timeLabel.pack()
playButton.pack(padx=10, side="left")
pauseButton.pack(padx=10, side="left")
stopButton.pack(padx=10, side="left")

simButton.pack(padx=20,side="right")
saveButton.pack(padx=20,side="right")
nextButton.pack(padx=20,side="right")
## 5 person

Person.canvas = canvas

p1 = Person(f1)
p2 = Person(f2)
p3 = Person(f3)
p4 = Person(f4)
p5 = Person(f5)
persons = [p1,p2,p3,p4,p5]

for song in mp3Files:
    songBox.insert('end', song)

for dat in datFiles:
    datBox.insert('end', dat)

canvas.mainloop()
mixer.quit()