from data import question_data  

# using list comprehension to store the questions and its correct answers in a list
correct_answers = [answers['correct_answer'] for answers in question_data ]     
questions = [question['question'] for question in question_data ]     
        
# print(correct_answers)
# print(questions)

# class for the game logic
class QuizBrain:
    def __init__(self, q_list, a_list):
        self.score = 0
        self.question_number = 0
        self.q_list = q_list
        self.a_list = a_list
        
    
    def still_has_questions(self):
        return self.question_number < len(self.q_list)
    
    def next_question(self):
        current_question = self.q_list[self.question_number]
        user_answer = input(f"Q. {self.question_number+1}) {current_question}\nIs the above statement (True/False): ")
        self.check_answer(self.a_list[self.question_number], user_answer)
        self.question_number += 1
    
    
    
    # method for checking answer
    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}\n")
        # print(f"Your current score is: {self.score}/{self.question_number}\n")
        


quiz = QuizBrain(questions, correct_answers)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number} ")