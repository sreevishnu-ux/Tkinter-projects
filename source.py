# importing the tkinter module
from tkinter import *

# importing the pyperclip module to use it to copy our generated
# password to clipboard
import pyperclip

# random module will be used in generating the random password
import random

# initializing the tkinter
gen = Tk()

# setting the width and height of the gui
gen.geometry("400x400")
gen.configure(bg='blue')
# declaring a variable of string type and this variable will be used to store the password generated
passstr = StringVar()

# declaring a variable of integer type which will be used to  store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate
    # the password
    passwords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length entered by the user
    for x in range(passlen.get()):
        password = password + random.choice(passwords)

    # setting the password to the entry widget
    passstr.set(password)
# function to copy the password to the clipboard


def copy():
    random_password = passstr.get()
    pyperclip.copy(random_password)


# Creating a text label widget
Label(gen, text="My Password Generator Application", font="aerial 15 bold", bg ='yellow').pack(pady=5, padx=5)

# Creating a text label widget
Label(gen, text="Enter the password length", fg ='black', font ="aerial 15 ", bg ='yellow').pack(pady=5, padx=5)

# Creating a entry widget to take password length entered by the
# user
Entry(gen, textvariable=passlen).pack(pady=5, padx=5)

# button to call the generate function
Button(gen, text="Generate Password", font ="aerial 15 ", command=generate, bg ='yellow').pack(pady=5, padx=5)

# entry widget to show the generated password
Entry(gen, textvariable=passstr).pack(pady=5, padx=5)

# button to call the copytoclipboard function
Button(gen, text="Copy to clipboard", font ="aerial 15 ", command=copy, bg ='yellow').pack(pady=5, padx=5)

gen.mainloop()