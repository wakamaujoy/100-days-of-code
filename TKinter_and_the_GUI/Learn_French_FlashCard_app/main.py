from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data= pandas.read_csv("./data/words_unknown")

except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

current_card =[]

def next_question():
    global current_card, flipper
    window.after_cancel(flipper)
    current_card= random.choice(data_dict)
    fr= current_card["French"]
    my_canvas.itemconfig(language,text= "French", fill ="black")
    my_canvas.itemconfig(word, text = fr, fill = "black")
    my_canvas.itemconfig(card_background, image = front_canvas)
    flipper = window.after(3000, func=flip_card)



def flip_card():
    en = current_card["English"]
    my_canvas.itemconfig(card_background, image=back_canvas)
    my_canvas.itemconfig(language, text="English", fill = "white")
    my_canvas.itemconfig(word, text=en, fill = "white")


def is_known():
    data_dict.remove(current_card)
    learnt_words = pandas.DataFrame(data_dict)
    learnt_words.to_csv("./data/words_unknown", index=4)
    print(len(learnt_words))

    next_question()



window = Tk()
window.title("Flashcard_App")
# window.config(pady=50, padx=50)
flipper= window.after(3000, func=flip_card)
window.config(bg= BACKGROUND_COLOR)

my_canvas = Canvas(width=800, height=620)
my_canvas.grid(column=0, row=0, columnspan=2)
my_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

front_canvas = PhotoImage(file= "./images/card_front.png")
back_canvas = PhotoImage(file="./images/card_back.png")
card_background = my_canvas.create_image(410, 310, image= front_canvas)

language = my_canvas.create_text(400,220, text="", font=("arial", 33,"bold"))
word= my_canvas.create_text(400,335, text="", font=("arial", 33,"bold"))

r_button = PhotoImage(file="./images/right.png")
right_button = Button(image=r_button, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)

w_button = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=w_button, highlightthickness=0, command=next_question)
wrong_button.grid(column=1, row=1)

next_question()


window.mainloop()
