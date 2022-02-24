def trainer():
    print('test')

import tkinter as tk
import random
from textwrap import fill

root = tk.Tk()
root.geometry('900x600')
root.config(bg='light green')
root.title('FPS trainer')

startButton = tk.Button(
    root,
    bg='white',
    text='start FPS trainer',
    font=("Courier", 14)
)
startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
startButton.configure(command=trainer)

root.mainloop()