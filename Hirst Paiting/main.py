from turtle import Turtle, Screen
from random import randint, choice
import random

'''import colorgram

colors = colorgram.extract('hirst_paiting.jpg',30)

rbg_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tupla = (r, g, b)
    rbg_colors.append(tupla)

print(rbg_colors)
'''

turtle = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    for color in color_list:
        pick_random_color = random.choice(color_list)
        r = pick_random_color[0]
        g = pick_random_color[1]
        b = pick_random_color[2]
        colors_rgb = (r, g, b)
        return colors_rgb

color_list = [(247, 241, 243), (135, 164, 199), (222, 151, 106), (31, 43, 63), (199, 137, 148), (158, 62, 52), (235, 212, 93), (50, 100, 140), (137, 180, 162), (147, 64, 72), (158, 32, 28), (50, 40, 44), (58, 49, 46), (62, 114, 99), (169, 28, 33), (228, 165, 170), (234, 168, 159), (209, 84, 73), (34, 60, 54), (15, 96, 71), (194, 99, 107), (172, 189, 219), (35, 61, 104), (109, 126, 157), (17, 82, 105), (175, 201, 190), (39, 149, 205)]
turtle.hideturtle()
turtle.right(90)
turtle.pensize(10)
value_y = 0


for x in range(10):
    value_x = -100
    turtle.teleport(value_x,value_y)
    for i in range(10):
        turtle.color(random_color())
        value_x += 20
        turtle.dot(10)
        turtle.teleport(value_x, value_y)
    value_y += 20

screen.exitonclick()
