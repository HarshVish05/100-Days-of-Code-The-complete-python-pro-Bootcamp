from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=500, height=500)
screen.title("Slow and Steady")
screen.tracer(0)

user = Player()
car  = Cars()
score = Scoreboard()


screen.listen()

screen.onkey(user.move, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    
    car.generate_car()
    car.move()
    
    
    # Detecting collision with cars
    for cars in car.all_cars:
        if cars.distance(user) < 20:
            game_on = False
            score.game_over()
            
    # Detecting if the turtle has crossed the road
    if user.ycor() > 240:
        user.reset_position()
        car.level_up()
        score.increase_level()










screen.exitonclick()