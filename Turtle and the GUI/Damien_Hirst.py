import random
import turtle as t
from turtle import Turtle, Screen
tim = Turtle()
t.colormode(255)
# direction = [0, 90, 180, 270]
#
#
# def color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tup = (r, g, b)
#     return tup
#
#
#
# tim.width(10)
# tim.speed(0)
# for _ in range(230):
#     tim.color(color())
#     tim.setheading(random.choice(direction))
#     tim.forward(40)


# import colorgram
# rgb_colors = []
# colors = colorgram.extract("images.jpeg", 40)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     rgb_colors.append(tup)

list_of_colors = [(137, 97, 42), (197, 157, 95), (165, 146, 54), (74, 9, 38), (12, 26, 70), (152, 12, 49), (244, 229, 239), (41, 101, 154), (44, 125, 80), (124, 164, 198), (124, 184, 152), (23, 42, 142), (142, 64, 98), (66, 40, 21), (55, 169, 123), (68, 107, 212), (18, 58, 37), (191, 141, 166), (19, 96, 58), (216, 205, 121), (83, 85, 18), (139, 221, 187), (197, 85, 126), (39, 164, 185), (121, 37, 28), (204, 95, 68), (9, 88, 104), (230, 167, 195), (170, 182, 228), (136, 215, 228), (224, 212, 12), (223, 177, 171), (36, 45, 234)]


def move():
    for _ in range(10):

        tim.dot(10, random.choice(list_of_colors))
        tim.forward(50)


tim.penup()
tim.setheading(225)
tim.forward(280)

for route in range(21):
    tim.setheading(0)
    move()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    move()



screen = Screen()
screen.exitonclick()

