from turtle import Turtle, Screen
screen = Screen()


class Refree(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
