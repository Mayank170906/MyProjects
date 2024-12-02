import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

scoreboard = Scoreboard()

screen = Screen()
screen.title("Turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
cars = []
player = Player()
screen.listen()
screen.onkey(player.move_f, "w")
screen.onkey(player.move_b, "s")
global level
level = 1


def game_on():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        if random.randint(0, 3) == 0:
            car = CarManager()
            cars.append(car)
        for i in range(len(cars)):
            cars[i].move(scoreboard)
        if player.ycor() > 300:
            scoreboard.level += 1
            global level
            level += 1
            game_is_on = False
            break
        i = 0
        while i < len(cars):
            if player.distance(cars[i]) < 20:
                scoreboard.level = 7
                game_is_on = False
                break
            i += 1


while scoreboard.level < 7:
    scoreboard.write(f"Level:{level}",
                     font=("Courier", 24, "normal"))
    game_is_on = True
    screen.tracer(0)
    player.goto(0, -280)
    screen.update()
    game_on()
    scoreboard.clear()
screen.clear()
screen.reset()
if level == 7:
    scoreboard.goto(-280, 0)
    scoreboard.write("Congratulations you won.",
                     font=("Courier", 30, "normal"))
else:
    scoreboard.goto(-280, 0)
    scoreboard.write(f"Oops you lost.\nLevel:{level}",
                     font=("Courier", 30, "normal"))

screen.exitonclick()
