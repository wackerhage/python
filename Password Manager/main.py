from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
from types import new_class

import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    letters = [choice(letters) for letter in range(randint(8, 10))]
    password_list.append("".join(letters))

    symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += symbols

    numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_list += numbers

    shuffle(password_list)
    password = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data = {
        input_website.get(): {
            "email": input_email_username.get(),
            "password": input_password.get(),
        }
    }

    if input_website.get() == "" or input_password.get() == "" or input_email_username.get() == "":
        empty_fields = messagebox.showerror(title="Oops!",
                                       message=f"There are missing fields.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            #updating
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)

# ---------------------------- PASSWORD FINDER SETUP ------------------------------- #

def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            # Reading old data
            data = json.load(data_file)
        for key, value in data.items():
            if input_website.get() != key:
                sorry = messagebox.showinfo(title="Here's what I got.", message=f"No details for this website, sorry.")
                break
            else:
                info = messagebox.showinfo(title="Here's what I got.", message=f"Email: {value['email']}  \n Password: {value['password']}")
                break
    except FileNotFoundError:
        no_data = messagebox.showinfo(title="Here's what I got.", message=f"No data file found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg= "white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,80, image=logo)
canvas.grid(column=2, row=0)

label_website = Label(text="Website:", fg="black", background="white")
label_website.grid(column=1, row=1)

label_email_username = Label(text="Email/Username:", fg="black", background="white")
label_email_username.grid(column=1, row=2)

label_password = Label(text="Password:", fg="black", background="white")
label_password.grid(column=1, row=3)

button_generate_password = Button(text="Generate Password", highlightbackground="white", command=generate_password)
button_generate_password.grid(column=3, row=3)

button_add = Button(text="Add", highlightbackground="white", width=45, command=save)
button_add.grid(column=2, row=4, columnspan=2)

button_search = Button(width=13, text="Search", highlightbackground="white", command=find_password)
button_search.grid(column=3, row=1)

input_website = Entry(width=30, background="white", highlightbackground="white", fg="black")
input_website.grid(column=2, row=1)

input_email_username = Entry(width=47, background="white", highlightbackground="white", fg="black")
input_email_username.grid(column=2, row=2, columnspan=2)

input_password = Entry(width=30, background="white", highlightbackground="white", fg="black")
input_password.grid(column=2, row=3)

input_website.focus()
input_email_username.insert(0, "wackerhaged@yahoo.com")

window.mainloop()