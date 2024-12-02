from turtle import Turtle, Screen
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.score = 0
        self.write(f"{self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def icrease_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center",
                   font=("Bold", 28, "normal"))
