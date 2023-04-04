from turtle import Turtle, Screen
from snake import Snake
from food import Food
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

snake = Snake()

snake.create_snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.home, "Left")
screen.onkey(snake.end, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
