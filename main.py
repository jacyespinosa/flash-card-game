from tkinter import *
from tkinter import Canvas

BACKGROUND_COLOR = "#B1DDC6"


#-----SET UP UI---#
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func='')

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
wrong_button = Button(image=wrong_image, highlightthickness=0, command='')
wrong_button.grid(column=0, row=3)

#Check Button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command='')

check_button.grid(column=1, row=3)


window.mainloop()

