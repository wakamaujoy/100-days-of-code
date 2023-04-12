from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('white')
        self.level = 1
        self.write(f"level:{self.level} ", align="center", font=("courier", 12, "normal"))

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"level:{self.level} ", align="center", font=("courier", 12, "normal"))

    def game_over(self):
        self.hideturtle()
        self.goto (0,0)
        self.color("white")
        self.write("GAME OVER", align="center", font=("courier", 12, "normal"))