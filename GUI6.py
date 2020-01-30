from tkinter import *

root = Tk() #blank window

def printname(event):
    print("My name is Anik")

#button=Button(root,text="Print My name", command=printname)
button=Button(root,text="Print My name")
button.bind("<Button-1>",printname)
button.pack()

root.mainloop() #unlimited looping