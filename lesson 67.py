#GUI windows
from tkinter import *

#widgets = GUI elements : buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets

window =Tk() #instantiate an instance of a window
window.geometry("420x420") #boyutu ayarla
window.title("Bro Code first GUI Program")

icon = PhotoImage(file='logo1.png')
window.iconphoto(True,icon)
window.config(background="#22f5ee")


window.mainloop() #place window on computer screen , listen for events

