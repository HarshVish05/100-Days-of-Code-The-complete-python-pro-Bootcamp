from tkinter import *
# Constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN= "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = 'Courier'
WORK_MIN = 1
SHORT_BREAK_MIN = 15
LONG_BREAK_MIN = 20
reps = 1
timer = None

#-------Reset Mechanism-------
def reset_timer():
    global reps
    window.after_cancel(timer) # to stop the countdown
    canvas.itemconfig(timer_text, text = "00:00")
    heading_label.config(text="Timer", fg= GREEN)
    check_label.config(text='')
    reps = 1

#---------Timer Mechanism---------

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN 
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        heading_label.config(text= "Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading_label.config(text= "Break", fg= PINK)
    else:
        count_down(work_sec)
        heading_label.config(text= "Work", fg= GREEN)
    reps += 1
    
#---------Countdown Mechanism------------
def count_down(count):
    
    count_min = count // 60
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1 )
    else:
        start_timer()
        marks = ''
        for _ in range(reps//2):
            marks += '✔'
            
        check_label.config(text= marks)

#---------------UI setup--------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)


canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file= 'tomato.png')
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
# canvas.pack()
canvas.grid(row=1, column=1)


heading_label = Label(text="Timer", bg= YELLOW, font= (FONT_NAME, 20, "bold"), fg= GREEN)
# heading_label.place(x=60, y=-30)
heading_label.grid(row=0, column=1)


start_button = Button(text="Start", highlightthickness= 0, command= start_timer)
# start_button.place(x= -30, y=200)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness= 0, command= reset_timer)
# reset_button.place(x= 190, y=200)
reset_button.grid(row=2, column=3)

check_label = Label( font= (FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)


window.mainloop()
