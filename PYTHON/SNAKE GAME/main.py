import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 700)
screen.tracer(0)
a = Snake()
a.move()
screen.exitonclick()
