from tkinter import *

root = Tk()

def my_click():
    myLabel1 = Label(root, text="Look, I clicked a Button")
    myLabel1.pack()

myButton = Button(root, text="Click Me", command=my_click())

myButton.pack()

root.mainloop()