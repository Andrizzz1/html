#part2
# import colorgram
import turtle
#
# colors = colorgram.extract("3.jpg", 6)
#
# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rgb_colors = (r, g, b)
#     list_of_colors.append(rgb_colors)
# print(list_of_colors)

#part2
from turtle import Turtle
from turtle import Screen
import random
turtle.colormode(255)
S = Screen()
T = Turtle()
T.speed("fastest")
T.penup()
T.hideturtle()
rgb_colors = [(254, 254, 254), (203, 34, 66), (71, 116, 151), (228, 161, 193), (246, 253, 251), (252, 246, 250)]
T.setheading(225)
T.forward(300)
T.setheading(0)
number_of_dots = 100

for _dots in range(1 , number_of_dots + 1):
    T.dot(20,random.choice(rgb_colors))
    T.forward(50)
    if _dots % 10 == 0:
        T.setheading(90)
        T.forward(50)
        T.setheading(180)
        T.forward(500)
        T.setheading(0)



S.exitonclick()
