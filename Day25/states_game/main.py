import turtle
import pandas

# def get_mouse_click_coor(x, y):    get the coordinates of mouse click
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
screen  = turtle.Screen()
screen.title("State Game")
screen.setup(800,700)


def write_state(answer, x_cor, y_cor):
    writer = turtle.Turtle() 
    writer.hideturtle()
    writer.penup()
    writer.goto(x_cor, y_cor)
    writer.write(answer,align='center', font=('Arial', 8, 'normal'))



image = "india.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("states.csv") 

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_state)}/50 states Correct", prompt="What's another state?").title()

    if answer_state == 'Exit':
        # used list comprehension
        missed_states = [state for state in data.state.to_list() if state not in guessed_state]
        
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')
        break
    
    state = data[data.state == answer_state]
    # print(day.y)
    if answer_state in data.state.to_list():
        guessed_state.append(answer_state)
        write_state(answer_state, int(state.x), int(state.y) )






# turtle.mainloop()  # alternative way to keep the window open

