from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.make_cars()


    def make_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 4:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            newy = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, newy)
            new_car.backward(self.car_speed)
            self.all_cars.append(new_car)
        else:
            pass


    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)



    def increase_speed(self):
        self.car_speed +=5









