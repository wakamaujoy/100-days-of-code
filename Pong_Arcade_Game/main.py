from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_score = ScoreBoard((-150, 280))
r_score = ScoreBoard((150, 280))

screen.listen()
screen.onkey(r_paddle.move_up, key="Up")
screen.onkey(r_paddle.move_down, key="Down")
screen.onkey(l_paddle.move_up, key="Left")
screen.onkey(l_paddle.move_down, key="Right")

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()
    ball.move()

    #Detect collission with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collission with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#       Detect whether the ball goes out of bounds, right side misses
    if ball.xcor() > 330:
        ball.restart()
        l_score.add_left_score()

    #  Detect whether the ball goes out of bounds, left side misses
    if ball.xcor() < -330:
        ball.restart()
        r_score.add_right_score()



screen.exitonclick()
