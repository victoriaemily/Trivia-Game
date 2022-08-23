from tkinter import *
from turtle import bgcolor
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width= 300,height=280, bg="white")
        
        self.score_label = Label(text = "Score = 0", fg = "white", bg=THEME_COLOR)
        self.score_label.grid(column = 1, row = 0)
        
        self.question_text = self.canvas.create_text(150,125,text='placeholder', width=250, font=("Arial", 15, "italic"), fill="black")
        self.canvas.grid(column = 0, row=1, columnspan=2, pady=50)
        
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, bd=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_question()
        
        self.window.mainloop()
        
    def get_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def true_pressed(self):
        status = self.quiz.check_answer("True")
        self.give_feedback(status)
        
    def false_pressed(self):
        status = self.quiz.check_answer("False")
        self.give_feedback(status)
        
    def give_feedback(self, is_right):
        print('yes')
        if is_right:
            print('yes')
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, text="You got that right!")
            self.score_label.config(text=f"Score = {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, text="You got that wrong!")
        self.window.after(1000,self.get_question)