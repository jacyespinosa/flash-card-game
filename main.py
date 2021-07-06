from tkinter import *
from tkinter import Canvas

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
data_list_of_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list_of_dict = original_data.to_dict(orient="records")
else:
    data_list_of_dict = data.to_dict(orient='records')

#Generate new random words
def generate_random_word():
    global random_word
    global flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_list_of_dict)
    random_french_word = random_word["French"]
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=random_french_word, fill='black')
    canvas.itemconfig(front_photo, image=card_front_photo)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    random_english_word = random_word['English']
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=random_english_word, fill='white')
    canvas.itemconfig(front_photo, image=card_back_photo)

def clicked_check():
    data_list_of_dict.remove(random_word)
    need_to_learn = pandas.DataFrame(data_list_of_dict)
    need_to_learn.to_csv('data/words_to_learn.csv', index=False)

    generate_random_word()

#-----SET UP UI---#
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Front Card
canvas = Canvas(width=800, height=526)
card_front_photo = PhotoImage(file="images/card_front.png")
front_photo = canvas.create_image(400, 263, image=card_front_photo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#Back Card
card_back_photo = PhotoImage(file="images/card_back.png")

#Title Text
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

#Word Text
word_text = canvas.create_text(400, 264, text="", font=("Arial", 50, "bold"))

#Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_random_word)
wrong_button.grid(column=0, row=3)

#Check Button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=clicked_check)
check_button.grid(column=1, row=3)

generate_random_word()

window.mainloop()

