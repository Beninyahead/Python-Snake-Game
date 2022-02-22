from turtle import Turtle
import time

HIGHSCORE_FILE = "high_score.txt"
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    """Class for writing, refreshing and tracking game score"""

    def __init__(self,height:int) -> None:
        super().__init__()
        self.is_game_on = True
        self.score = 0
        self.high_score = 0
        self.HEIGHT = height
        self.penup()
        self.hideturtle()
        self.__read_high_score()
        self.__update_scoreboard()
    
    def __update_scoreboard(self):
        """Update the Scoreboard with current score and highscore"""
        self.color('white')
        self.goto(0,self.HEIGHT/2-35)
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by one, then update scoreboard"""
        self.score += 1
        self.__update_scoreboard()
    
    def __reset_scoreboard(self):
        """Reset the Scoreboard. 
        If current score greater than highscore, update the highscore"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.__write_high_score()
        self.score = 0
        self.__update_scoreboard()
    
    def __read_high_score(self):
        """Read highscore txt file to self.highscore"""
        with open(HIGHSCORE_FILE, mode='r', encoding='utf-8') as file:
            self.high_score = int(file.read())

    def __write_high_score(self):
        """Write the highscore to txt file, overwriting existing data"""
        with open(HIGHSCORE_FILE, mode='w', encoding='utf-8') as file:
            file.write(f'{self.high_score}')
    
    def game_over(self):
        """Game Over method, reset the game"""
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.clear()
        self.__reset_scoreboard()