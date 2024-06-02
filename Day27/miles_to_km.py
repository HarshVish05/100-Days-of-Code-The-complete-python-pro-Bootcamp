from tkinter import *

window = Tk()
window.title("Converter")
# window.minsize(width=300, height= 200)
window.config(padx= 20, pady=20)


entry = Entry(width=10)
entry.grid(row=1, column=1)


miles_label = Label(text= "Miles")
miles_label.grid(row=1, column=2)

equal_label = Label(text= "is equal to")
equal_label.grid(row=2, column=0)

answer_label = Label(text="0")
answer_label.grid(row=2, column=1)

km_label = Label(text="KM")
km_label.grid(row=2, column=2)

def calculate():
    km = float(entry.get())*1.6
    answer_label.config(text= km)

button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=1)








window.mainloop()