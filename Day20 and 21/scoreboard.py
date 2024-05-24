from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        # self.goto(0, 260)
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT) 
        
        
    def increment(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)