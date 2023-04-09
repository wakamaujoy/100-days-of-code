from turtle import Turtle
r_paddle = (350, 0),
l_paddle = (-350, 0)


class Paddle(Turtle,):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed("fastest")


    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_yy = self.ycor() - 20
        self.goto(self.xcor(), new_yy)
