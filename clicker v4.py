from textwrap import fill
import tkinter
from tkinter import CENTER,N,S

number = 0
ifPressed = 0

def tripleScore():
    global number,ifPressed
    if ifPressed == 1:
       number *= 3
    elif ifPressed == 2:
        number /= 3   
    displayNumber.config(text=number)
        
def hoverMouse():
    root.config(bg='yellow')
def unHover():
    global number
    if number == 0:
        root.config(bg='grey')
    elif number > 0:
        root.config(bg='green')
    elif number < 0:
        root.config(bg='red')
    displayNumber.config(text=number)

def numUp():
    global number,ifPressed
    number += 1
    ifPressed = 1
    if number == 0:
        root.config(bg='grey')
    elif number > 0:
        root.config(bg='green')
    elif number < 0:
        root.config(bg='red')
    displayNumber.config(text=number)

def numDown():
    global number,ifPressed
    number -= 1
    ifPressed = 2
    if number == 0:
        root.config(bg='grey')
    elif number > 0:
        root.config(bg='green')
    elif number < 0:
        root.config(bg='red')
    displayNumber.config(text=number)

root = tkinter.Tk()
root.config(bg='grey')
root.geometry('400x350')
root.title('Clicker')
root.bind('<Up>',lambda event:numUp()),root.bind('+',lambda event:numUp())
root.bind('<Down>',lambda event:numDown()),root.bind('-',lambda event:numDown())
root.bind('<space>',lambda event:tripleScore())

buttonUp=tkinter.Button(root)
buttonUp.configure(text='Up',font=("Courier", 14),anchor=N,command = numUp)
buttonUp.pack(fill='x',padx=40,pady=60)
buttonUp.bind('<Enter>',lambda event: hoverMouse())
buttonUp.bind('<Leave>',lambda event: unHover())

displayNumber = tkinter.Label(
    root,
    bg='white',
    text=number,
    font=("Courier", 14),
)
displayNumber.pack(fill='x',padx=40)
displayNumber.bind('<Enter>',lambda event: hoverMouse())
displayNumber.bind('<Leave>',lambda event: unHover())
displayNumber.bind('<Double-Button-1>',lambda event:tripleScore())

buttonDown=tkinter.Button(root)
buttonDown.configure(text='Down',font=("Courier", 14),anchor=S, command=numDown)
buttonDown.pack(fill='x',padx=40,pady=60)
buttonDown.bind('<Enter>',lambda event: hoverMouse())
buttonDown.bind('<Leave>',lambda event: unHover())

root.mainloop()