from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as file:
            data = file.read()
            self.highscore = int(data)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score:{self.score}\nHigh Score:{self.highscore}", align="center",
                   font=("Arial", 24, "normal"))

    def icrease_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}\nHigh Score:{self.highscore}", align="center",
                   font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.clear
        self.write(f"Score:{self.score}\nHigh Score:{self.highscore}", align="center",
                   font=("Arial", 24, "normal"))
