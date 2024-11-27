from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.write((0,0), True)
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
    
    def write_score(self):
        self.clear()
        self.write(f"your score: {self.score}", align='center', font=('Arial', 22, 'normal'))
    
    def score_up(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f'GAME OVER, Your score was: {self.score}', align='center',  font=('Arial', 22, 'normal'))