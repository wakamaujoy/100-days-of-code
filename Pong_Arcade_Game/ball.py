from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.x = 10
        self.y = 10

    def move(self):
        newx = self.xcor() + self.x
        newy = self.ycor() + self.y
        self.penup()
        self.goto(newx, newy)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()
