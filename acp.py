from tkinter import *
from datetime import date

root = Tk()
root.title('Check in')
root.geometry('400x200')

lbl = Label(text="Type your full name to sign up to this workshop", fg="white", bg="#800080", height=1, width=400)

name_entry = Entry()

def display():
    name = name_entry.get()
    
    global message
    message = "Welcome to this workshop! \n Today's date is: "
    greet = "Hello "+ name+ "\n"
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
    
text_box = Text(height=3)

btn = Button(text="Check in", command = display, height = 1, bg = "#CBC3E3", fg="white")

lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()