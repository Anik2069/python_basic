from tkinter import *

root = Tk()
topframe= Frame (root)
topframe.pack()
buttom= Frame(root)
buttom.pack(side=BOTTOM)

button1 = Button(topframe,text ="Button 1" , fg="red")
button2 = Button(topframe,text ="Button 2" , fg="red")
button3 = Button(topframe,text ="Button 3" , fg="red")
button4 = Button(buttom,text ="Button 4" , fg="red")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)
root.mainloop()