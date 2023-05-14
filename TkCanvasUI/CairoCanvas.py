import tkinter as tk
from mod.slider import Slider


root = tk.Tk()
root.geometry('500x500')

n = Slider(root)
n.pack()

root.mainloop()
