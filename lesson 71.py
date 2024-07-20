#Checkbox

from tkinter import *

def display():
    if(x.get()==1):
        print("you agree :)")
    else:
        print("You don't agree :(")


window = Tk()

x= IntVar() #sayı yerine true Bfalse kullansaydık BooleanVar() kullanmlıydık

python_photo = PhotoImage(file='pythonlogo.png')
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1, # bu kısımlarda
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=10,
                           image= python_photo,
                           compound='left'
                           )
check_button.pack()

window.mainloop()