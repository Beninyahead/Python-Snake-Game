from turtle import Screen, Turtle, xcor
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600
SEG_SIZE = 15

X_COLLISION = WIDTH/2 - SEG_SIZE
Y_COLLISION = HEIGHT/2 - SEG_SIZE


# Screen:
screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# set up Turtle instances:
snake = Snake()
food = Food(WIDTH, HEIGHT)
score = Scoreboard(HEIGHT)

# Screen listener functions
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
# Basic game loop, refresh every 0.1 second
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food compare two turtles
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    # detect colison with walls:
    if (snake.head.xcor() > X_COLLISION or snake.head.xcor() < -X_COLLISION 
        or snake.head.ycor() > Y_COLLISION or snake.head.ycor() < -Y_COLLISION):
        score.game_over()
        score.reset()
        snake.reset()

    # detect colision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()