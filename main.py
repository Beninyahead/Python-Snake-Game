from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600
COLLISION_SEG_SIZE = 15

X_COLLISION = WIDTH/2 - COLLISION_SEG_SIZE
Y_COLLISION = HEIGHT/2 - COLLISION_SEG_SIZE

# Set up game screen:
screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Set up Turtle game objects:
snake = Snake()
food = Food(WIDTH, HEIGHT)
score = Scoreboard(HEIGHT)

# Setup screen listener functions
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

def game_over():
    """Reset the Snake Game"""
    score.game_over()
    snake.reset()

game_is_on = True
# Basic game loop, refresh every 0.1 second
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food compare two turtles
    if snake.head.distance(food) < COLLISION_SEG_SIZE:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    # detect colison with walls:
    if (snake.head.xcor() > X_COLLISION or snake.head.xcor() < -X_COLLISION 
        or snake.head.ycor() > Y_COLLISION or snake.head.ycor() < -Y_COLLISION):
        game_over()

    # detect colision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < COLLISION_SEG_SIZE:
            game_over()

screen.exitonclick()