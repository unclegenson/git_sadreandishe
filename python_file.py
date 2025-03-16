import tkinter as tk
import random

window = tk.Tk()
window.geometry('200x300')

dices = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
dice = ''

l = tk.Label(window,text=dice,font=('times',100))
l.pack()

def roll():
  global dices
  l.config(text=str(random.choice(dices)))

b = tk.Button(text='roll',font=('times',20),command=roll)
b.pack()

window.mainloop()




