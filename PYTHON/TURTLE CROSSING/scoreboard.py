from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(-280, 250)
