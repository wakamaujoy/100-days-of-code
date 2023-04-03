from turtle import Turtle, Screen
import time

screen = Screen()

screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
# timmy1 = Turtle()
# timmy2 = Turtle()
# timmy3 = Turtle()
#
# timmy1.color("white")
# timmy1.shape("square")
# timmy1.goto(0, 0)
#
# timmy2.color("white")
# timmy2.shape("square")
# timmy2.goto(-20, 0)
#
# timmy3.color("white")
# timmy3.shape("square")
# timmy3.goto(-40, 0)
screen.tracer(0)
directions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for segment in directions:
    new_segment = Turtle()
    new_segment.color("white")
    new_segment.shape("square")
    new_segment.penup()
    new_segment.goto(segment)
    segments.append(new_segment)
screen.update()

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    for piece in range(len(segments) - 1, 0, -1):
        newx = segments[piece - 1].xcor()
        newy = segments[piece - 1].ycor()
        segments[piece].goto(newx, newy)
    segments[0].forward(100)


screen.exitonclick()
