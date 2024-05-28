from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.score = 0
        with open('data.txt',mode='r') as file:
            self.high_score = int(file.read())
        self.update_score()
 
        
    def update_score(self):
        self.clear()
        # self.goto(0, 260)
        self.write(f"Score: {self.score} High Score {self.high_score}", align= ALIGNMENT, font=FONT) 

            
    def increment(self):
        self.score += 1
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align= ALIGNMENT, font=FONT)
        
    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode= 'w') as file:
                file.write(str(self.high_score))
            
        self.score = 0
        self.update_score()
            
    