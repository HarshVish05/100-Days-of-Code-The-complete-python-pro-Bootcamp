from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")

timmy.color('cyan')
t.colormode(255)

# print(timmy.pencolor())

# timmy.circle(50)
# timmy.teleport(60)
# timmy.circle(50)

# challenge 1 - Draw a square

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# challenge 2 - Draw a dashed line

# for i in range(4):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
# timmy.forward(40)

# challenge 3 - Draw a triangle, square, pentagon, hexagon, heptagon, nonagon, octagon, decagon
colors = ['red','cyan','blue','green','purple','yellow','black','aqua','red','cyan','blue','green','purple','yellow','black','aqua']
# color_counter = 0
# timmy.teleport(-100,100)
# for sides in range(3,11):
#     angle = 360 / sides
#     timmy.pencolor(colors[color_counter])
#     for i in range(0,sides):
#         timmy.left(angle)
#         timmy.back(100)
#     color_counter += 1


# challenge - 4  Generate a random walk


# direction = [0, 90, 180, 270]

# timmy.width(5)
# timmy.speed('fastest')
# for _ in range(100):
#     timmy.pencolor((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
#     timmy.seth(random.choice(direction))
#     timmy.forward(30)
    
# challenge 5 - Make a spirograph

for i in range(0,1000,10):
    timmy.circle(100)
    timmy.seth(i)
    




screen = Screen()
screen.exitonclick()