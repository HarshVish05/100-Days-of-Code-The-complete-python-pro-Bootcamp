# below code was to extract colors from image using module colorgram
# import colorgram

# colors = colorgram.extract('color_image.jpg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

colors = [(249, 241, 235), (215, 163, 65), (250, 220, 229), (234, 65, 120), (243, 222, 74), (218, 237, 222), (236, 64, 44), (247, 234, 0), (213, 131, 178), (166, 81, 43), (102, 182, 224), (53, 106, 165), (203, 221, 231), (243, 162, 184), (8, 159, 76), (32, 175, 76), (166, 79, 152), (1, 111, 60), (81, 36, 30), (91, 191, 163), (100, 120, 185), (150, 212, 206), (198, 162, 40), (137, 31, 27), (79, 65, 44), (146, 211, 215), (232, 172, 163), (179, 185, 219), (133, 31, 33), (83, 37, 39)]

# hirst painting

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def draw_circle():
    tim.fillcolor(random.choice(colors))
    tim.begin_fill()
    tim.pencolor(random.choice(colors))
    tim.circle(10)
    tim.end_fill()

tim.penup()
a = -200
b = 200
tim.goto(a,b)
for i in range(10):
    for _ in range(10):
        draw_circle()
        tim.teleport()
        tim.forward(40)
    b -= 40
    tim.goto(a, b)

tim.hideturtle()
# tim.dot(20)


    
    

    
    
    
    


screen = Screen()
screen.exitonclick()