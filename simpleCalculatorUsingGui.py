import tkinter as tk  
from functools import partial  

def add(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  

def subtract(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)-int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  
def multiply(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)*int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  
def divison(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)/int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  

root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="First Number:").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="Second Number:").grid(row=2, column=0)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
add = partial(add, labelResult, number1, number2)
subtract = partial(subtract, labelResult, number1, number2)
multiply = partial(multiply, labelResult, number1, number2)
divison = partial(divison, labelResult, number1, number2) 
  
buttonCal1 = tk.Button(root, text="Add", command=add).grid(row=3, column=0)
buttonCal2 = tk.Button(root, text="Subract", command=subtract).grid(row=3, column=1)
buttonCal3 = tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=2)
buttonCal4 = tk.Button(root, text="Division", command=divison).grid(row=4, column=1)  
  
root.mainloop()  