import time
import turtle, pandas
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
list_states = data["state"].to_list()
correct_guesses = []
missing_guesses = list_states
turtle = turtle.Turtle()
score = ScoreBoard()

while len(correct_guesses) != 50:
    screen.update()
    time.sleep(0.2)
    score.update_scoreboard()

    answer_state = screen.textinput(title=f"Correct guesses: {len(correct_guesses)}/50", prompt="What's another state's name?").title()

    if answer_state ==  "Exit":
        data = pandas.DataFrame(missing_guesses)
        data.to_csv("missing_guesses")
        score.reset_score()
        break
    if answer_state in list_states:
        correct_guesses.append(answer_state)
        missing_guesses.remove(answer_state)
        score.increase_score()
        row = (data[data.state == answer_state])
        x = row.x.values[0]
        y = row.y.values[0]
        turtle.penup()
        turtle.goto((x, y))
        turtle.hideturtle()
        turtle.write(arg=answer_state)
    if correct_guesses == 50:
        final_message = screen.textinput(title="Congratulations!", prompt="You got all of them!!!")
        break
