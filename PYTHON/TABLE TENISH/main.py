from paddle import Paddle
from turtle import Turtle, Screen
from ball import Ball
import time
from scoreboard import Scoreboard
from refree import Refree

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
a = Paddle(300, 0)
b = Paddle(-300, 0)
ball = Ball()
scoreboard_a = Scoreboard(50, 270)
scoreboard_b = Scoreboard(-50, 270)
screen.listen()
screen.onkey(a.up, "w")
screen.onkey(a.down, "s")
screen.onkey(b.up, "Up")
screen.onkey(b.down, "Down")
ball.move()
is_true = True
speed_ball = 0.1
while is_true:
    time.sleep(speed_ball)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    if ball.distance(a) < 25:
        speed_ball *= 0.9
        ball.bounce_x()
    if ball.distance(b) < 25:
        speed_ball *= 0.9
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.reset_position()
        speed_ball = 0.1
        scoreboard_b.icrease_score()
    if ball.xcor() < -390:
        ball.reset_position()
        speed_ball = 0.1
        scoreboard_a.icrease_score()
    if scoreboard_b.score > 10:
        refree = Refree()
        refree.goto(-200, 150)
        scoreboard_b.game_over()
        refree.write("You won", font=("Arial", 24, "normal"))
        break
    if scoreboard_a.score > 10:
        refree = Refree()
        refree.goto(200, 150)
        scoreboard_a.game_over()
        refree.write("You won", font=("Arial", 24, "normal"))
        break


screen.exitonclick()
