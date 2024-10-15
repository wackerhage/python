from turtle import Turtle
from food import Food

ALIGNMENT = "center"
MOVE = False
FONT = "Courier", 20, "normal"

score = 1

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = score
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.change_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", MOVE, ALIGNMENT, FONT)


    def change_score(self):
        self.write(f"Score: {self.score}", MOVE, ALIGNMENT, FONT)
        self.score += 1
