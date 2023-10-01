from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")

def add():
    num1 = int(input1.get())
    num2 = int(input2.get())
    sum = num1+num2
    resultLabel["text"] = "The result is "+str(sum)

label1 = Label(root, text="Enter the first number:")
label1.place(relx=0.2, rely=0.1, anchor=CENTER)

label2 = Label(root, text="Enter the second number:")
label2.place(relx=0.2, rely=0.2, anchor=CENTER)

input1 = Entry(root)
input1.place(relx=0.65, rely=0.1,anchor=CENTER)

input2 = Entry(root)
input2.place(relx=0.65, rely=0.2,anchor=CENTER)

resultLabel = Label(root, text="")
resultLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

addButton = Button(root, text="Add", command = add)
addButton.place(relx=0.5, rely=0.4,anchor=CENTER)


root.mainloop()

