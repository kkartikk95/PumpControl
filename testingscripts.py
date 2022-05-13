from tkinter import *
import os
from subprocess import call
import threading

def test():
    pmpaddr = adr.get()
    print(pmpaddr)
    if pmpaddr ==1:
        threading.Thread(target=call, args=("python testpy1.py",), ).start()
    if pmpaddr==2:
        threading.Thread(target=call, args=("python testpy2.py",), ).start()




root = Tk()
root.title("IL-2 PK SIMULATION")
root.geometry("800x800")

file = Entry(root, width=45)
file.pack()
myButton = Button(root, text="Choose a CSV File")
myButton.pack(pady=20)

log = Entry(root, width=45)
log.pack(pady=5)
button2 = Button(root, text="Create log file")
button2.pack()

adr = IntVar()
adr.set("Select Pump")
pumpaddr = OptionMenu(root, adr, 1, 2, 3, 4, 5, 6)
pumpaddr.pack(pady=10)

start = Button(root, text="Start Program", command=test)
start.pack(side=LEFT, padx=210)

cancel = Button(root, text="Cancel Program")
cancel.pack(side=LEFT)

root.mainloop()
