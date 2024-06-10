from tkinter import *
import pandas
import random

BACKGROUND_COLOR = '#B1DDC6'

#---------Reading the data---------
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')

to_learn = data.to_dict(orient='records')
# print(dict_data)
current_card = {}


#------creating new cards-------
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # cancelling the previous flip timer
    
    # if there is nothing in to_learn
    if len(to_learn) == 0:
        card_canvas.itemconfig(main_title, text = 'No More cards', fill = 'black')
        card_canvas.itemconfig(word, text = '', fill = 'black')
        return
        
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(main_title, text = 'French', fill = 'black')
    card_canvas.itemconfig(word, text = current_card['French'], fill = 'black')
    card_canvas.itemconfig(card_background, image = card_image_front)


    # Flipping the cards after 3s
    flip_timer = window.after(3000, func= flip_card)
    
#-----Removing the card--------
def remove_card():
    if current_card in to_learn:
        to_learn.remove(current_card)
    new_card()

#---------Saving the remaining words-------
def save():
    data_to_save = pandas.DataFrame(to_learn)
    data_to_save.to_csv('./data/words_to_learn.csv',index= False)
    window.destroy()

# ------Flipping the card-----
def flip_card():
    card_canvas.itemconfig(card_background, image = card_image_back)
    card_canvas.itemconfig(main_title, text = 'English', fill = 'white')
    card_canvas.itemconfig(word, text = current_card['English'], fill = 'white')
    


#-------UI setup--------
window = Tk()
window.title("Anki Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.protocol("WM_DELETE_WINDOW", save)    

flip_timer = window.after(3000, func= flip_card)

card_canvas = Canvas(width= 800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = './images/card_front.png'
back_image = './images/card_back.png'
card_image_front = PhotoImage(file= front_image)
card_image_back = PhotoImage(file= back_image)
card_background = card_canvas.create_image(402, 263, image = card_image_front)

# text in card
main_title = card_canvas.create_text(400, 150, font=("Ariel",40,"italic"), text= "")
word = card_canvas.create_text(400, 270, font=("Ariel",60,"bold"), text='')
card_canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image= wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command= new_card)
wrong_button.grid(row= 1, column=0)

right_image = PhotoImage(file='./images/right.png')
right_button = Button(image= right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command= remove_card)
right_button.grid(row=1, column=1)

new_card()      # calling this here so when we run the code we see a card instead of heading and word
 


window.mainloop()