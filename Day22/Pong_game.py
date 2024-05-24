from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # this method is used for turning off the animation used in goto method


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        
    # Detect collision with right paddle
    # we have used less than 50 because when distance is calculated its calculated from centre of the turtle and suppose the ball hits the top op paddle then the distance might be more thats why we have used 50
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when ball goes off the bounds from right paddle
    if ball.xcor() > 390:
        ball.reset_position()
        score.increment_left()
        
    # the reason we are using seperate if for left and right cause we have to increase the score
        
    # Detect when ball goes off the bounds from left paddle
    if ball.xcor() < -400:
        ball.reset_position()
        score.increment_right()











screen.exitonclick()