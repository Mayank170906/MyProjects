from turtle import Turtle, Screen
import random
# name = ["tim", "yim", "uim", "iim", "oim"]
colors = ["red", "yellow", "green", "blue", "pink"]
characters = []
for i in range(5):
    character = Turtle(shape="turtle")
    characters.append(character)
    characters[i].penup()
    characters[i].color(colors[i])
    characters[i].goto(x=-300, y=-100+50*i)
screen = Screen()
screen.listen()
is_true = False


def user():
    global user_bet
    user_bet = screen.textinput(title="Bet", prompt="Make your bet")
    return user_bet


while True:
    if user() in colors:
        is_true = True
        break
    else:
        user()


def race():
    while is_true:
        for i in range(5):
            characters[i].forward(random.randint(0, 10))
            if characters[i].xcor() > 300:
                global winner
                winner = characters[i]
                return characters[i]


if race() == user_bet:
    winner.write("You won", align="center", font=("Arial", 16, "normal"))
else:
    winner.write("You lost", align="center", font=("Arial", 16, "normal"))
    winner.write(f"The winner is {winner}")
screen.exitonclick()
