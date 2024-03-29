from turtle import Turtle
MOVE = 20
DIRECTIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for segment in DIRECTIONS:
            self.extend(segment)

    def extend(self, segment):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segment)
        self.segments.append(new_segment)


    def add_seg(self):
        self.extend(self.segments[-1].position())

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.segments= []
        self.create_snake()


    def move(self):
        for piece in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[piece - 1].xcor()
            newy = self.segments[piece - 1].ycor()
            self.segments[piece].goto(newx, newy)
        self.segments[0].forward(MOVE)


    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def home(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def end(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)



