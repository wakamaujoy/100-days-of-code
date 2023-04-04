from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
food = Food()
score = Scoreboard()

snake.create_snake()
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
    if snake.segments[0].distance(food) < 12:
        food.refresh()
        score.add_score()



screen.exitonclick()
