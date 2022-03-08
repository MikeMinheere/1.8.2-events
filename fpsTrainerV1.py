#de list voor knoppen die je moet klikken
randomAction=['<space>','a','w','s','d','<Double-Button-1>','<Triple-Button-1>' ]

import tkinter as tk
import random

#hier word de score toegevoegd na een actie
def addScore():
    random.shuffle(randomAction)
        
    global score
    score = 0
    score += 1
    scoreLabel.place(x=840, y = 15)
    scoreLabel['text'] = score
    pressNumber['text'] = randomAction[0]

def countdown(count):
    label.place(x=35, y=15)
    # verander de tektst in de label 
    label['text'] = count
    if count > 0:
        # call de countdown opnieuw na 1 seconden
        root.after(1000, countdown, count-1)
    elif count == 0:
        root.destroy()

#de plek waar de gehele trainer in komt
def trainer():
    countdown(20)
    pressNumber['text'] = randomAction[0]
    scoreLabel.pack()
    pressNumber.pack()
    pressNumber.place(x= random.randint(0,850), y = random.randint(0,550))
    startButton.destroy()

#dit is de configuration
root = tk.Tk()
root.geometry('900x600')
root.config(bg='light green')
root.title('FPS trainer')

#hier word de startknop gemaakt
startButton = tk.Button(
    root,
    bg='white',
    text='start FPS trainer',
    font=("Courier", 14)
)

#dit is de label die ik gebruik om de 'testen' uit te voeren.
pressNumber = tk.Label(
root,
bg='white',
text='random',
font=("Courier", 14)
)

#voor de score
scoreLabel = tk.Label(
root,
bg = 'light green',
font=('courier', 14)
)

#voor de timer
label = tk.Label(
root,
bg='light green',
font=('courier', 14)
)

#plek van de knop
startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
startButton.configure(command=trainer)

if randomAction[0] != '<Double-Button-1>' or randomAction[0] != '<Triple-Button-1>':
    root.bind(randomAction[0],lambda event:addScore())

root.mainloop()