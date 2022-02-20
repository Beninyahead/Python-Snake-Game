from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        # set up the snake
        self.SEGMENT_SIZE = 20
        self.STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
        self.snake_segments = []
        self.create_snake()


    def create_snake(self):
        for position in self.STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.snake_segments[0]
        self.head.color('green')
        
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.snake_segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
    
    def move(self):
        # for range of starting at len of list, and ending at 0, iterating by -1 each time.
        for seg_num in range(len(self.snake_segments)-1, 0, -1):
            # X and Y coordinates need to be the corridantes of the segment in front.
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(self.SEGMENT_SIZE)
    
    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)


    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000,1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

