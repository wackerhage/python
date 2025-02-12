from tkinter import Button, PhotoImage, Tk, Canvas, Label
import json
import pandas as pd
from mypyc.primitives.list_ops import to_list
from pandas import read_csv
from pandas.core.computation.align import align_terms
from random import randint, random
import time

BACKGROUND_COLOR = "#B1DDC6"

#------------------------- READING .CSV ------------------------------#

try:
    data = pd.read_csv("./data/words_to_learn.csv")
# print(df["English"][1])
except FileNotFoundError:
    data = pd.read_csv("./data/english.csv")
finally:
    list_words_en = data['English'].tolist()
    list_words_pt = data['Portuguese'].tolist()

#-----------------------GENERATING RANDOM WORDS AND DELETE------------------------#

def random_word():
    global random_number
    random_number = randint(1, 1000)
    return list_words_en[random_number - 1], list_words_pt[random_number - 1]

def delete_word():
    global random_number
    list_words_en.pop(random_number - 1)
    list_words_pt.pop(random_number - 1)

    new_data = {
        'English': list_words_en,
        'Portuguese': list_words_pt
    }

    df = pd.DataFrame(new_data)
    df.to_csv("./data/words_to_learn.csv", index=False)

#-----------------FLIPPING CARDS AND UPDATING TEXTS--------------------#

def update_text():
    global word_en, word_pt, flip_timer
    word_en, word_pt = random_word()
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=img_card_front)
    canvas.itemconfig(title, fill="black", text="English", font=("Arial", 40, "italic"))
    canvas.itemconfig(word, fill="black", text=word_en, font=("Arial", 60, "bold"))
    flip_timer = window.after(3000, flipping)

def update_text_and_delete_old_word():
    global word_en, word_pt, flip_timer
    delete_word()
    word_en, word_pt = random_word()
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=img_card_front)
    canvas.itemconfig(title, fill="black", text="English", font=("Arial", 40, "italic"))
    canvas.itemconfig(word, fill="black", text=word_en, font=("Arial", 60, "bold"))
    flip_timer = window.after(3000, flipping)

def flipping():
    global word_pt
    canvas.itemconfig(canvas_image, image=img_card_back)
    canvas.itemconfig(title, text="Portuguese", fill="white")
    canvas.itemconfig(word, fill="white", text=word_pt)

#-----------------------USER INTERFACE (UI)---------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flipping)

# Creating Images
img_card_front = PhotoImage(file="./images/card_front.png")
img_card_back = PhotoImage(file="./images/card_back.png")
img_right =  PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")

# Import Images
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400,266, image=img_card_front)
canvas.grid(column=1, row=1, columnspan=2)

# Buttons
correct_button = Button(image=img_right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=update_text_and_delete_old_word)
correct_button.grid(column=2, row=2)
wrong_button = Button(image=img_wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=update_text)
wrong_button.grid(column=1, row=2)

# Texts
title = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Welcome", font=("Arial", 60, "bold"), fill="black")
update_text()

window.mainloop()

