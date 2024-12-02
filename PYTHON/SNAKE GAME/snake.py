from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import Scoreboard
food = Food()
scoreboard = Scoreboard()


class Snake:

    def __init__(self):
        self.snake_body = []
        for i in range(3):
            self.snake_part = Turtle("square")
            self.snake_part.penup()
            self.snake_part.goto(-20*i, 0)
            self.snake_part.color("white")
            self.snake_body.append(self.snake_part)

    def new_snake(self):
        for i in range(len(self.snake_body)):
            self.snake_body[i].goto(1000, 1000)
        self.snake_body.clear()
        for i in range(3):
            self.snake_part = Turtle("square")
            self.snake_part.penup()
            self.snake_part.goto(-20*i, 0)
            self.snake_part.color("white")
            self.snake_body.append(self.snake_part)

    def move(self):
        def movement(x):
            if x != 0:
                x_cor, y_cor = self.snake_body[x-1].pos()
                self.snake_body[x].goto(x_cor, y_cor)
            else:
                self.snake_body[x].forward(20)
        screen = Screen()

        def up():
            self.snake_body[0].setheading(90)

        def left():
            self.snake_body[0].setheading(180)

        def down():
            self.snake_body[0].setheading(270)

        def right():
            self.snake_body[0].setheading(0)
        screen.listen()
        screen.onkey(up, "w")
        screen.onkey(down, "s")
        screen.onkey(left, "a")
        screen.onkey(right, "d")
        is_true = True

        def extend_snake():
            self.snake_part = Turtle("square")
            self.snake_part.penup()
            self.snake_part.goto(self.snake_body[-1].position())
            self.snake_part.color("white")
            self.snake_body.append(self.snake_part)

        while is_true:
            screen = Screen()
            screen.update()
            time.sleep(0.1)
            for i in range(len(self.snake_body)-1, -1, -1):
                movement(i)
            if self.snake_body[0].distance(food) < 15:
                food.new_food()
                scoreboard.icrease_score()
                extend_snake()

            else:
                pass
            if self.snake_body[0].xcor() > 290 or self.snake_body[0].xcor() < -290:
                scoreboard.clear()
                scoreboard.reset()
                self.new_snake()
            elif self.snake_body[0].ycor() > 290 or self.snake_body[0].ycor() < -290:
                scoreboard.clear()
                scoreboard.reset()
                self.new_snake()
            else:
                pass
            for i in range(1, len(self.snake_body)):
                if self.snake_body[0].distance(self.snake_body[i]) < 10:
                    scoreboard.clear()
                    scoreboard.reset()
                    self.new_snake()
                    break
