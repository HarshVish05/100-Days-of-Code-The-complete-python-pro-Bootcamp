from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 80, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align= ALIGNMENT, font= FONT)
        self.goto(100, 200)
        self.write(self.right_score, align= ALIGNMENT, font= FONT)
        
        
    def increment_left(self):
        self.left_score += 1
        self.update_scoreboard()
        
    def increment_right(self):
        self.right_score += 1
        self.update_scoreboard()