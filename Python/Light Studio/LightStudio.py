from tkinter import*
from tkinter import colorchooser

time = 0
colorData = []
hatColour = []
shirtColour = []
pantColour = []
gloveColour = []
shoeColour = []

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
