import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as my_file:
            self.high_score = int(my_file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w")as my_file:
                my_file.write(f"{self.high_score}")


        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGH SCORE:{self.high_score}", align="center", font=("Arial", 12, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", move=False, align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()




