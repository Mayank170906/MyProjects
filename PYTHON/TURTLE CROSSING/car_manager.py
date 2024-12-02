from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.goto(300, random.randint(-250, 300))

    def move(self, scoreboard):
        self.backward(STARTING_MOVE_DISTANCE+scoreboard.level*MOVE_INCREMENT)
