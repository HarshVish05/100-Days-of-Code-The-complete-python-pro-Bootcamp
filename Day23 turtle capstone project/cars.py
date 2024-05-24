from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Cars:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        
        
    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-150, 150)
            new_car.goto(230,random_y) 
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)
            
    def level_up(self):
        self.move_distance  += MOVE_INCREMENT