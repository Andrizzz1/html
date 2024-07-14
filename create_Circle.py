import turtle as t
from turtle import Screen

import random

S = Screen()

tim = t.Turtle()
t.colormode(255)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


########### Challenge 5 - Spirograph ########
def size_of_circle(enter_size):
    for _ in range(int(360/enter_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + enter_size)
        tim.circle(100)


size_of_circle(5)
screen = S.exitonclick()