from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def move_f(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_b(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
