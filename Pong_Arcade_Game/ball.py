from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)


    def move(self):
        newx = self.xcor() + 10
        newy = self.ycor() + 10
        self.penup()
        self.goto(newx, newy)


