from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"


def canvas_fn(title, word, img):
    global canvas
    canvas = Canvas(height=526, width=800,
                    background=BACKGROUND_COLOR, highlightthickness=0)
    canvas.create_image(400, 263, image=img)
    canvas.create_text(400, 150, text=title,
                       font=('Ariel', 40, 'italic'))
    canvas.create_text(400, 263, text=word, font=('Ariel', 60, 'bold'))
    canvas.grid(row=0, column=0, rowspan=2, columnspan=2)
    display.update()


def next_word():
    global canvas, timer
    global french_word
    del timer
    try:
        del canvas
    except:
        pass
    title = "French"
    word = random.choice(list_French)
    french_word = word
    index = list_French.index(word)
    canvas_fn(title, word, card_front_img)
    timer = display.after(3000)
    flip(index)


def flip(index):
    global canvas, english_word
    del canvas
    word = list_English[index]
    english_word = word
    title = 'English'
    canvas_fn(title, word, card_back_img)


def right():
    global list_French
    list_French.remove(french_word)
    next_word()


display = Tk()
display.title("Flash Card")
display.config(width=900, height=700,
               background=BACKGROUND_COLOR, highlightthickness=0, padx=50, pady=50)
display.minsize(800, 526)
card_back_img = PhotoImage(file='./images/card_back.png')
card_front_img = PhotoImage(file='./images/card_front.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

button_right = Button(highlightthickness=0,
                      background=BACKGROUND_COLOR, image=right_img, command=right)
button_wrong = Button(highlightthickness=0,
                      background=BACKGROUND_COLOR, image=wrong_img, command=next_word)
button_right.grid(row=2, column=0)
button_wrong.grid(row=2, column=1)

try:
    data = pandas.read_csv('./data/unlearnt.csv')
    list_French = [i for i in data['French']]
    list_English = [i for i in data['English']]
except:
    data = pandas.read_csv('./data/french_words.csv')
    list_French = [i for i in data['French']]
    list_English = [i for i in data['English']]

timer = display.after(1)
next_word()

display.mainloop()

my_dict = {french: english for french,
           english in zip(list_French, list_English)}
df = pandas.DataFrame(list(my_dict.items()), columns=['French', 'English'])
df.to_csv('./data/unlearnt.csv', index=False)
