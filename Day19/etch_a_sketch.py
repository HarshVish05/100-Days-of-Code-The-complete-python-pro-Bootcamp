from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forwards():
    tim.forward(100)
    
def backwards():
    tim.backward(100)

def turn_left():
    tim.left(10)
    
def turn_right():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_drawing)




screen.exitonclick()