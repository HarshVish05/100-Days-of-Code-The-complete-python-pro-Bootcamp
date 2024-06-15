from tkinter import *
import requests

def get_quotes():
    res = requests.get("https://api.kanye.rest", verify=False)
    quote = res.json()['quote']
    canvas.itemconfig(qoute_text, text = quote)


window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50)


canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file='background.png')
canvas.create_image(150, 207, image = background_img)
qoute_text = canvas.create_text(150, 207, text= "Quote goes here", font=("Arial", 30, "bold"), width=250)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file='kanye.png')
kanye_button = Button(image= kanye_img, highlightthickness=0, command= get_quotes)
kanye_button.grid(row=1, column=0)





window.mainloop()