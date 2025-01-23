from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition((-280,270))
        self.write(arg="Level: " + str(self.level), align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg="Level: " + str(self.level), align="left", font=FONT)

    def game_over(self):
        game_over = Turtle()
        self.penup()
        self.hideturtle()
        self.setposition((0,0))
        self.write(arg="GAME OVER", align="center", font=FONT)