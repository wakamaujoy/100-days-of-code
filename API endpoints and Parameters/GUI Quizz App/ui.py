from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question
import time

THEME_COLOR = "#375362"


def get_question(self):
    quizz = self.quiz.next_question
    self.canvas.itemconfig(qsn, text=quizz)


def right_answer(self):
    if self.quiz.check_answer(self.correct):
        self.get_question()


class QuizzlerUI():
    def __init__(self, q_brain:QuizBrain):
        self.quiz = q_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)


        self.my_label = Label(text=f"score:0", bg=THEME_COLOR, fg="white")
        self.my_label.grid(column=1, row=0)



        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.qsn = self.canvas.create_text(150, 125,width=250, text="", font=("arial", 20, "italic"))


        right = PhotoImage(file="images/true.png")
        self.correct = Button(image=right, highlightthickness=0, command=self.true)
        self.correct.grid(column=0, row=2)

        wrong = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong, highlightthickness=0, command=self.false)
        self.wrong.grid(column=1, row=2)

        self.get_question()


        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.my_label.config(text=f"score:{self.quiz.score}/{self.quiz.question_number}")
            quizz = self.quiz.next_question()
            self.canvas.itemconfig(self.qsn, text=quizz)
        else:
            self.canvas.itemconfig(self.qsn, text ="Game Over!")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")


    def true(self):
        self.feedback(self.quiz.check_answer("True"))

    def false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_question)





