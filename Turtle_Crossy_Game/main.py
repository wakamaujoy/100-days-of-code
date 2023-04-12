import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.make_cars()
    car.move()

#     Detect collission with car
    for carss in car.all_cars:
        if player.distance(carss) < 20:
            game_is_on = False
            score.game_over()
#
#Detect player on the other side  of the screen
    if player.ycor() > 270:
        player.goto(0,-280)
        score.next_level()
        car.increase_speed()


screen.exitonclick()