from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        screen.tracer(0)
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 2.5)
        self.goto(x_cor, y_cor)
        self.color("white")
        self.setheading(90)
        self.move_steps = 25
        screen.update()

    def up(self):
        if self.ycor() < 380:
            self.forward(self.move_steps)
            screen.update()

    def down(self):
        if self.ycor() > -380:
            self.backward(self.move_steps)
            screen.update()
