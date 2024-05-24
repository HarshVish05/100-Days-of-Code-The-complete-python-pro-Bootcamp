from turtle import Turtle

POS = (0, -200)
MOVE_DISTANCE = 10
# FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(POS)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def reset_position(self):
        self.goto(POS)