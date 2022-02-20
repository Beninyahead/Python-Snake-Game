from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, WIDTH, HEIGHT) -> None:
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        rand_x = random.randint(self.WIDTH/-2 + 20, self.WIDTH/2 - 20)
        rand_y = random.randint(self.HEIGHT/-2 + 20, self.HEIGHT/2 - 20)
        self.goto(rand_x,rand_y)
    
    def refresh(self):
        rand_x = random.randint(self.WIDTH/-2 + 20, self.WIDTH/2 - 20)
        rand_y = random.randint(self.HEIGHT/-2 + 20, self.HEIGHT/2 - 20)
        self.goto(rand_x,rand_y)
    
