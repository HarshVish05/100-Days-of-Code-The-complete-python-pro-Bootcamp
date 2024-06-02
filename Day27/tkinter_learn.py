# args

# def add (*args):
#     result = 0
#     for n in args: # args is a tuple
#         result += n
#     return result

# print(add(2,3,4))

# kwargs
# def calculate(n, **kwargs):
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     # print(kwargs['add'])
#     print(n)
# calculate(5, add = 5 , multiply = 7)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw['make']
#         self.model = kw.get('model')

# my_car = Car(make = 'Nissan')   
# print(my_car.model)


import tkinter

window = tkinter.Tk()

window.title("The first GUI program")
window.minsize(width=500, height= 300)
window.config(padx= 20, pady= 20)

# label
my_label = tkinter.Label(text="First label", font= ('Arial', 24, 'bold'))
# my_label.pack()  # to display the label on screen
# my_label.place(x=0, y=100)
my_label.grid(column=0, row=0)  # think of all the program is divided into rows and coloums and it will not work with pack at all
my_label.config(padx=20, pady=20)
# my_label['text'] = 'New text'
# my_label.config(text='New text')


# Button
def button_clicked():
    my_label.config(text= entry.get())   # text='Button got clicked

button = tkinter.Button(text= 'Click Me', command= button_clicked)
# button.pack()
button.grid(column=1, row=1)
# button.config(padx=20, pady=20)

# challenge make my label to read button got clicked when the button gets clicked


# Entry
entry = tkinter.Entry(width= 10)
# entry.pack()
entry.grid(column=2, row=2)
entry.get()  # to get hold of whatever is written in input


# challenge make the label read whatever is written in input after button is clicked

# textbox
text = tkinter.Text(width=10, height=10)
# puts cursor in the box
text.focus()
# add something in the box to begin with
text.insert(tkinter.END, "Example of multiline string")
# get whatever is written on the first line
print(text.get("1.0", tkinter.END))
# text.pack()

# spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_= 0, to= 10, width= 5, command= spinbox_used )
# spinbox.pack()

# Scale
def scale_used(value): # this funciton by def gets 1 argument
    print(value)

scale = tkinter.Scale(from_=0, to= 10, command= scale_used)
# scale.pack()

# checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton  = tkinter.Checkbutton(text= 'Is On?', variable= checked_state, command= checkbutton_used)
# checkbutton.pack()

# Radiobuttons
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text= 'option1', value=1, variable= radio_state, command= radio_used)
radiobutton2 = tkinter.Radiobutton(text= 'option2', value=2, variable= radio_state, command= radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# ListBox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ['Apple', 'Banana', "Mango"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()  # to keep the window there


