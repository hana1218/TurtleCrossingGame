from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = random.randint(0,50)


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

        
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        random_chance = random.randint(0,1)
        if random_chance == 1:
            cars = Turtle()
            cars.shape("square")
            cars.penup()
            cars.shapesize(stretch_len=2,stretch_wid=1)
            cars.color(random.choice(COLORS))
            cars.goto(300, random.randint(-250,250))
            self.all_cars.append(cars)

    def level_up(self):
        self.car_speed +=MOVE_INCREMENT

        


