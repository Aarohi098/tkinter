#import necessary libraries
from tkinter import *
from datetime import date

#create window
root = Tk()
root.title('Getting started with widgets')
root.geometry('400x300')

#add widgets
#add label
lbl = Label(text="Hey there!", fg="white", bg="#072F5F", height=1, width=300)

#add label for getting name as input from user
#use entry widget to create a text box for user to enter details
name_lbl = Label(text="Full Name:", bg="#3895D3")
name_entry = Entry()

#function to display a message
def display():
    #read input given by user
    name = name_entry.get()
    
    #declaring a global variable
    #to make it accessible anywhere in the program
    global message
    message = "Welcome to the Application! \n Today's date is: "
    greet = "Hello "+ name+ "\n"
    
    #display details in a text box
    #specify where to add the details in a text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
    
#add a text widget to display info/ messages
text_box = Text(height=3)

#add button and give value of command as name of the function
#press button, display function will be called automatically
btn = Button(text="Begin", command = display, height = 1, bg = "#1261A0", fg="white")

#organise all the widgets into the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

#start the GUI event loop
root.mainloop()