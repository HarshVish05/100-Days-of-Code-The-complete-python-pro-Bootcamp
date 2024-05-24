from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

    
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Wakey Wakey Snakey! It's eating time....")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()   # to update the screen
    time.sleep(0.1)   # the above 2 lines means refresh the screen after every 0.1s
    
    snake.move()
    
    # Detect collision with food.
    if snake.head.distance(food) < 15:  # 15 because the food(turtle) itself is size of 10 so we have added a bit of buffer, we can also tweak it a lil bit for more accuraacy
        food.refresh()
        score.increment()
        snake.extend()
        
    # Detect collision with bouondary wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False
        
    # Detect collision with tail
    # if head collides with any body segment then game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
        







screen.exitonclick()
