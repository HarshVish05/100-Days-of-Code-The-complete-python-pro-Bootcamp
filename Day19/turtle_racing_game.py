from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Place your bet", prompt="Which color turtle you want?")
# print(user_choice)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

y = -100
turtles = []
for i in range(len(colors)):
    t = Turtle('turtle')
    t.penup()
    t.color(colors[i])
    t.goto(-230, y)
    y += 40
    turtles.append(t)


is_race_on = False

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_choice == winning_color:
                print(f"Congratulation! your turtle won the race. The {winning_color} has won the race")
            else:
                print("Sorry! your turtle lost the race")
            is_race_on = False
        dist = random.randint(0, 10)
        turtle.forward(dist)
        
    
    


screen.exitonclick()