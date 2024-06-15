from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR, padx=20, pady=20)
        
        self.score_label = Label(text= f"Score: {self.quiz_brain.score}", bg= THEME_COLOR, fg= 'white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.quiz_text = self.canvas.create_text(150, 125, width= 280, text="Somethin", font=("Arial", 15, "italic"), fill= THEME_COLOR)
        self.canvas.grid(row= 1, column=0, columnspan=2, pady=50)

        true_button_image = PhotoImage(file= "./images/true.png")
        self.true_button = Button(image= true_button_image, highlightthickness=0, bg= THEME_COLOR, command= self.true_clicked)
        self.true_button.grid(row=2, column=0)

        false_button_image = PhotoImage(file= "./images/false.png")
        self.false_button = Button(image= false_button_image, highlightthickness=0, bg= THEME_COLOR, command= self.false_clicked)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        # resetting the canvas to white after an answer
        self.canvas.config(bg= 'white')
        
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quiz_text, text = q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text = "You've reached the end of the game.")
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")
        
    def true_clicked(self):
        self.check_answer_correct("True")
        # self.quiz_brain.check_answer("True")

    def false_clicked(self):
        self.check_answer_correct("False")
        # self.quiz_brain.check_answer("False")
        
    def check_answer_correct(self, user_answer):
        answer = self.quiz_brain.check_answer(user_answer)
        if answer:
            self.canvas.config(bg= 'green')
        else:
            self.canvas.config(bg= 'red')

        self.score_label.config(text= f"Score: {self.quiz_brain.score}")
        self.window.after(1000, self.get_next_question)
        
    # def give_feedback(self):
    #     self.canvas.config(bg= "green")