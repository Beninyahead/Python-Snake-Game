from turtle import Turtle
import random

SEG_SIZE = 20

class Food(Turtle):
    """Class for generatign the snakes food on the board"""
    def __init__(self, width:int, height:int) -> None:
        self.WIDTH = width
        self.HEIGHT = height
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)

        self.refresh()
    
    def refresh(self):
        """Refresh the position of the food on the screen"""
        rand_x = random.randint(self.WIDTH/-2 + SEG_SIZE, self.WIDTH/2 - SEG_SIZE)
        rand_y = random.randint(self.HEIGHT/-2 + SEG_SIZE, self.HEIGHT/2 - SEG_SIZE)
        self.goto(rand_x,rand_y)
    
