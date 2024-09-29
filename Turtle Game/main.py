import turtle
from turtle import Turtle, Screen
import random
from tkinter import messagebox


def reset():
    for i in range(len(turtles)):
        turtles[i].goto(x=-200, y=y_positions[i])


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
game = True

turtle_red = Turtle(shape="turtle")
turtle_orange = Turtle(shape="turtle")
turtle_yellow = Turtle(shape="turtle")
turtle_green = Turtle(shape="turtle")
turtle_blue = Turtle(shape="turtle")
turtle_purple = Turtle(shape="turtle")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
turtles = [turtle_red, turtle_orange, turtle_yellow, turtle_green, turtle_blue, turtle_purple]

for i in range(len(colors)):
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-200, y=y_positions[i])

if user_bet:
    race = True

while game is True:
    while race is True:
        for i in range(6):
            distance = random.randint(0, 10)
            turtles[i].forward(distance)
            if turtles[i].xcor() >= 150:
                print(turtles[i].pencolor())
                if turtles[i].pencolor() == user_bet:
                    print("You won!")
                    messagebox.showinfo("", "You won!")
                    race = False
                    break
                else:
                    print("You lost")
                    messagebox.showinfo("", "You lost!")
                    race = False
                    break

    play_again = messagebox.askyesno("Reset?")
    if play_again is True:
        race = True
        reset()
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        print(user_bet)
        continue
    elif play_again is False:
        messagebox.showinfo("", "Good bye!")
        break

screen.exitonclick()
