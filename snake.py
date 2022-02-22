from turtle import Turtle

# Direction degrees
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Class for creating and controlling the snake"""
    def __init__(self) -> None:
        # set up the snake
        self.SEGMENT_SIZE = 20
        self.STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
        self.snake_segments = []
        self.__create_snake()

    def __create_snake(self):
        """Create the name at starting positions"""
        for position in self.STARTING_POSITIONS:
            self.__add_segment(position)
        self.head = self.snake_segments[0]
        self.head.color('green')
        
    def __add_segment(self, position):
        """Add a new snake segment at the given position"""
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.snake_segments.append(new_segment)
    
    def extend(self):
        """Extend the snake by one segment at the end"""
        self.__add_segment(self.snake_segments[-1].position())
    
    def move(self):
        """Move the snake forward in its current direction by one segment"""
        # for range of starting at len of list, and ending at 0, iterating by -1 each time.
        for seg_num in range(len(self.snake_segments)-1, 0, -1):
            # X and Y coordinates need to be the corridantes of the segment in front.
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(self.SEGMENT_SIZE)
    
    def up(self):
        """Turn the snake up"""
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        """Turn the snake down"""
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def right(self):
        """Turn the snake right"""
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def left(self):
        """Turn the snake left"""
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def reset(self):
        """Reset the snakes length and go to starting postion"""
        for segment in self.snake_segments:
            segment.goto(1000,1000)
        self.snake_segments.clear()
        self.__create_snake()
