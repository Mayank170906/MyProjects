from turtle import Turtle, Screen
import random
import time
screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10

    def bounce_y(self):
        self.y_cor *= -1
        self.move()

    def bounce_x(self):
        self.x_cor *= -1
        self.move()

    def move(self):
        x = self.xcor()+self.x_cor
        y = self.ycor()+self.y_cor
        self.goto(x, y)

    def reset_position(self):
        x = 0
        y = 0
        self.goto(x, y)
        self.x_cor = 10
        self.y_cor = 10
