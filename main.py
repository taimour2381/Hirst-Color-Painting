import colorgram
from turtle import Turtle, Screen
import random

color_extractor = colorgram.extract('hirst_painting.jpg', 30)
rgb_color = []
print(color_extractor)

for color in color_extractor:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

print (rgb_color)
color_list = [(186, 20, 46), (243, 233, 64), (252, 232, 237), (221, 241, 246), (193, 76, 36), (217, 68, 108), (20, 124, 170), (15, 142, 89), (195, 175, 20), (109, 182, 208), (15, 166, 212), (206, 155, 92), (26, 40, 74), (179, 44, 64), (36, 43, 110), (79, 174, 96), (236, 231, 4), (215, 68, 49), (216, 130, 154), (125, 184, 120), (236, 162, 181), (9, 61, 39), (148, 209, 220), (9, 90, 52), (6, 85, 108), (155, 31, 29), (235, 171, 164), (161, 211, 186)]
screen = Screen()
screen.colormode(255)
screen.setup(width=700, height=700)
screen.title("Hirst Painting")

outline = Turtle()
outline.hideturtle()
outline.speed(0)
outline.penup()
outline.goto(-345, -345)
outline.pendown()
outline.pencolor("black")
for n in range(4):
    outline.forward(670)
    outline.left(90)

turtle = Turtle("circle")
turtle.hideturtle
turtle.pensize(10)
turtle.penup()
turtle.speed(0)
x = -325
y = -325
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = -255
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = -185
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = -115
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = -45
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = 25
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = 95
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = 165
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = 235
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)
x = -325
y = 305
turtle.goto(x, y)
for n in range(10):
    turtle.color(random.choice(color_list))
    turtle.stamp()
    turtle.forward(70)

turtle.color("white")

screen.exitonclick()