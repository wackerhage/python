from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.setposition(STARTING_POSITION)

