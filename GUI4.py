from tkinter import *

root = Tk() #blank window

l1= Label(root,text="Name")
l2= Label(root,text="Password")
e1= Entry(root)
e2= Entry(root)

l1.grid(row=0)
l2.grid(row=1)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

c=Checkbutton(root, text="keep me logged in")
c.grid(columnspan=2)

root.mainloop() #unlimited looping