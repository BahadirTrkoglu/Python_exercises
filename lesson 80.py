#Menubar

from tkinter import *

def openFile():
    print("Fİle has been opened! ")
def saveFile():
    print("File has been saved!")

def cut():
    print("You cut some text!")

def copy():
    print("You copy some text!")


def paste():
    print("You paste some text!")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()# çizgi ekliyor
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


window.mainloop()




