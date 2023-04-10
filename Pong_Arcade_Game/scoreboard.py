from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.goto(direction)
        self.write(f"score:{self.l_score}", align="center", font=("courier", 12, "normal"))


    def add_left_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"score:{self.l_score}", align="center", font=("courier", 12, "normal"))

    def add_right_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"score:{self.r_score}", align="center", font=("courier", 12, "normal"))

    # def l_score(self):



