import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()


    def update_score(self):
        self.write(f"SCORE:{self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()




