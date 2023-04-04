import random
from turtle import Turtle
random_x = random.randint(-280, 280)
random_y = random.randint(-280, 280)



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.goto(random_x, random_y)
