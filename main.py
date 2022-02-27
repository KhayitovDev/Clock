from tkinter import *
from tkinter.ttk import *

from time import strftime

main=Tk()
main.title('Digital Clock')

def clock():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, clock)

label=Label(main, font=('ds-digital', 90), background='black', foreground='yellow')
label.pack(anchor='center')

clock()

mainloop()