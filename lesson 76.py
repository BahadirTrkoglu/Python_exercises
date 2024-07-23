from tkinter import *
from tkinter import colorchooser #submodule

def click():
   color =  colorchooser.askcolor()
   print(color)
   colorHex = color[1]
   print(colorHex)
   window.config(bg=colorHex) #change background color

#window.config(bg=colorchooser.askcolor()[1]) # tek satırda

window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click )
button.pack()
window.mainloop()