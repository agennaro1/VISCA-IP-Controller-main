 


import tkinter as tk
 
window = tk.Tk()
window.title('My Window')
window.geometry('500x300') 
 
l = tk.Label(window, bg='blue', fg='black', width=20, text='empty')
l.pack()
 
def print_selection(v):
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
 
window.mainloop()


# Este me gusta 
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Playing with Scales")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

slider = int()

ttk.Scale(mainframe, from_=0, to_=17, length=200,  variable=slider).grid(column=1, row=4, columnspan=5)
ttk.Label(mainframe, textvariable=slider).grid(column=1, row=0, columnspan=5)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()



from tkinter import *

def show_values():
    print (w1.get(), w2.get())


master = Tk()
w1 = Scale(master, from_=0, to=42, tickinterval=8)
w1.set(19)
w1.pack()
w2 = Scale(master, from_=0, to=200,tickinterval=10, orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()


