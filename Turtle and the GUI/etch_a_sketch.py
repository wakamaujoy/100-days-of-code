from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.back(20)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
screen.listen()
screen.onkey(move_forwards, "f")
screen.onkey(move_left, "l")
screen.onkey(move_backwards, "b")
screen.onkey(move_right, "r")
screen.onkey(clear, "c")



screen.exitonclick()