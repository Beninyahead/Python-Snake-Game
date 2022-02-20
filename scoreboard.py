from turtle import Screen, Turtle
import time

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self,HEIGHT) -> None:
    
        super().__init__()
        self.is_game_on = True
        self.score = 0
        self.high_score = 0
        self.HEIGHT = HEIGHT
        self.penup()
        self.hideturtle()
        self.read_high_score()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.color('white')
        self.goto(0,self.HEIGHT/2-35)
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()
    
    def read_high_score(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
    def write_high_score(self):
        with open("high_score.txt",mode='w') as file:
            file.write(f'{self.high_score}')
    
    # removed
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()