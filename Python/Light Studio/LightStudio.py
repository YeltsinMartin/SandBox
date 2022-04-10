from abc import abstractmethod
import tkinter as tk
from tkinter import *
import os
from pygame import mixer
from tkinter import colorchooser
import sqlite3

class Database:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT * FROM songTable")
            self.cur.fetchone()
        except:
            self.cur.execute('''CREATE TABLE songTable (
                                                        name VARCHAR(255),
                                                        data BLOB)''')

    def getData(self, name)-> list:
        self.cur.execute("SELECT data FROM songTable WHERE name =:name",{'name':name})
        return self.cur.fetchone()

    def getNames(self) ->list:
        self.cur.execute("SELECT name FROM songTable")
        return self.cur.fetchall()
        
    def updateData(self,name, data) -> None:
        '''This method can UPDATE or INSERT data into the db'''
        if self.getData(name):
            self.cur.execute("UPDATE songTable SET data =:data WHERE name =:name",{'name':name, 'data':data})
        else:
            self.cur.execute("INSERT INTO songTable VALUES (:name, :data)",{'name':name, 'data':data})
        self.conn.commit()

    def close(self) ->None:
        #print("DB closed")
        self.conn.close()

class popupWindow:
    def __init__(self,canvas):
        self.value=None
        self.top=tk.Toplevel(canvas, bg ="black")
        self.l=tk.Label(self.top,text="Enter data name:", fg = "cyan", bg ="black")
        self.l.pack()
        self.e=tk.Entry(self.top, fg = "cyan", bg ="black")
        self.e.pack()
        self.b=tk.Button(self.top,text='Save',command=self.cleanup, fg = "cyan", bg ="black")
        self.b.pack()
    
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
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

        self.capImg   =  tk.PhotoImage(file="Resources\\cap.png")
        self.shirtImg =  tk.PhotoImage(file="Resources\\shirt.png")
        self.shoeImg  =  tk.PhotoImage(file="Resources\\shoe.png")
        self.gloveImg =  tk.PhotoImage(file="Resources\\glove.png")
        self.pantImg  =  tk.PhotoImage(file="Resources\\pant.png")

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

    def resetColours(self) ->None:
        self.capButton.config(bg='black')
        self.shirtButton.config(bg='black')
        self.pantButton.config(bg='black')
        self.gloveButton.config(bg='black')
        self.shoeButton.config(bg='black')
        Person.canvas.update()

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

class MediaPlayer:
    time = 0
    playing = False
    colorData = []
    mp3Files = []
    datFiles = []



    def __init__(self,lightDatabase,f0, f6 , canvas, persons) -> None:
        mixer.init()
        #try anchor
        self.lightDatabase = lightDatabase
        self.f0 = f0
        self.f6 = f6
        self.canvas =  canvas
        self.persons = persons
        self.playImg  = tk.PhotoImage(file="Resources\\play.png")
        self.pauseImg = tk.PhotoImage(file="Resources\\pause.png")
        self.stopImg  = tk.PhotoImage(file="Resources\\stop.png")
        self.simImg   = tk.PhotoImage(file="Resources\\sim.png")
        self.saveImg  = tk.PhotoImage(file="Resources\\save.png")
        self.nextImg  = tk.PhotoImage(file="Resources\\next.png")

        self.songBox = tk.Listbox(self.f0, fg = "green", bg ="black", width=50)
        self.datBox = tk.Listbox(self.f0, fg = "cyan", bg ="black", width=50)

        self.songLabel = tk.Label(self.f6, text="", fg = "yellow", bg ="black", font="Ebrima 14")
        self.songLabel.pack()

        self.timeLabel  = tk.Label(self.f6, text="TIME: {0} seconds".format(MediaPlayer.time), bg="black",fg = "cyan", borderwidth=0, font="Ariel 14")
        self.nextButton = tk.Button(self.f6, text = "Next Frame", command = self.saveTime, image=self.nextImg, bg="black", borderwidth=0)
        self.saveButton = tk.Button(self.f6, text = "Save Data" , command = self.saveData, image=self.saveImg, bg="black", borderwidth=0)
        self.simButton  = tk.Button(self.f6, text = "Play"      , command = self.simCmd, image=self.simImg, bg = "black", borderwidth=0)

        self.playButton  = tk.Button(self.f6, text = "Play", command=self.playCmd, image=self.playImg, bg = "black", borderwidth=0)
        self.pauseButton = tk.Button(self.f6, text = "Pause", command=self.pauseCmd, image=self.pauseImg, bg = "black", borderwidth=0)
        self.stopButton  = tk.Button(self.f6, text = "Stop", command=self.stopCmd, image=self.stopImg, bg = "black", borderwidth=0)

        self.songBox.pack(padx=10, pady=10)
        self.datBox.pack(padx=10, pady=10)
        self.timeLabel.pack()
        self.playButton.pack(padx=10, side="left")
        self.pauseButton.pack(padx=10, side="left")
        self.stopButton.pack(padx=10, side="left")
        self.simButton.pack(padx=20,side="right")
        self.saveButton.pack(padx=20,side="right")
        self.nextButton.pack(padx=20,side="right")

        self.findMedia()
        self.updateMedia()
        
    def resetColurs(self) ->None:
        for person in self.persons:
            person.resetColours()

    def updateMedia(self) -> None:
        self.songBox.delete(0,END)
        for song in MediaPlayer.mp3Files:
            self.songBox.insert('end', song[1:]) #to get rid of the leading backslash

        self.datBox.delete(0,END)
        for data in MediaPlayer.datFiles:
            self.datBox.insert('end', data[0])

    def findMedia(self) -> None:
        MediaPlayer.mp3Files.clear()
        MediaPlayer.datFiles.clear()

        cwd = os.getcwd()
        for r, fo, fi in os.walk(os.getcwd()):
            MediaPlayer.mp3Files.extend([r.replace(cwd,"")+"\\"+file for file in fi  if file.find(".mp3") != -1])
        
        MediaPlayer.datFiles.extend(self.lightDatabase.getNames())

    def playCmd(self) -> None:
        if not MediaPlayer.playing:
            self.songLabel.config(text= self.songBox.get("anchor"))
            mixer.music.load(os.getcwd()+"\\"+self.songBox.get("anchor"))
            mixer.music.play()
            MediaPlayer.playing = True
        else:
            mixer.music.unpause()

    def pauseCmd(self) -> None:
        mixer.music.pause()

    def stopCmd(self) -> None:
        mixer.music.stop()
        self.songLabel.config(text="")
        self.songBox.select_clear('active')
        MediaPlayer.playing= False

    def saveTime(self):
        global time
        MediaPlayer.time += 1
        data = []
        for person in persons:
            data.append(person.getData())
        #print(data) ##commented for debugging
        MediaPlayer.colorData.append(data)
        self.timeLabel.config(text="TIME: {0} seconds".format(MediaPlayer.time))
        self.canvas.update()

    def saveData(self):
        popUp=popupWindow(self.canvas)
        self.saveButton["state"] = "disabled" 
        self.canvas.wait_window(popUp.top)
        self.saveButton["state"] = "normal"
        if popUp.value:
            self.lightDatabase.updateData(popUp.value, str(MediaPlayer.colorData))
        self.findMedia()
        self.updateMedia()
        MediaPlayer.time = 0
        self.timeLabel.config(text="TIME: {0} seconds".format(MediaPlayer.time))
        self.resetColurs()
        self.canvas.update()

    def simCmd(self) -> None:
        pass

    def close(self) -> None:
        #print("Mixer closed")
        mixer.quit()

canvas = tk.Tk()
canvas.title("Light Studio")
canvas.geometry("800x600")
canvas.config(bg='black')


lightDatabase = Database()

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

## 5 person
Person.canvas = canvas
p1 = Person(f1)
p2 = Person(f2)
p3 = Person(f3)
p4 = Person(f4)
p5 = Person(f5)
persons = [p1,p2,p3,p4,p5]

mediaPlayer = MediaPlayer(lightDatabase,f0, f6, canvas, persons)

canvas.mainloop()
mediaPlayer.close()
lightDatabase.close()

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
