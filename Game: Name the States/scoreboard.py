from turtle import Turtle

ALIGNMENT = "center"
MOVE = False
FONT = "Courier", 20, "normal"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.read_file()
        self.score = 0
        self.highscore = 1
        self.update_scoreboard()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0,270)

    def read_file(self):
        with open("data.txt", mode="r") as file:
            self.highscore = file.read()

    def write_file_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))

    def update_scoreboard(self):
        self.clear()
        self.read_file()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            self.write_file_highscore()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
