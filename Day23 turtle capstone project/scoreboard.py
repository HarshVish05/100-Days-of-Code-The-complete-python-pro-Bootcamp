from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-220, 200)
        self.level = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font= FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font= FONT)