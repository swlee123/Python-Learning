THEME_COLOR = "#375362"
CANVAS_COLOR = "#FFF7B7"

import tkinter as tk
from quiz_brain import QuizBrain
import time



class Quizinterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.geometry("420x500")
        self.image1 = tk.PhotoImage(file=r"true.png")
        self.image2 = tk.PhotoImage(file=r"false.png")

        self.canvas = tk.Canvas()
        self.canvas.config(bg=CANVAS_COLOR)
        self.question = self.canvas.create_text(150, 100,fill="black", text="I am pro",font=("Ariel", 20, "italic"),width=300)
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        self.score = 0
        self.score_label = tk.Label(fg = "white",text=f"Score: {self.quiz.score}",font=("Ariel", 10, "normal"),bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.right_button = tk.Button(image=self.image1)
        self.right_button.config(height=100, width=100,highlightthickness=0,command=self.click_right)
        self.right_button.grid(column=0, row=2)
        self.wrong_button = tk.Button(image=self.image2)
        self.wrong_button.config(height=100, width=100,highlightthickness=0,command=self.click_wrong)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_COLOR)
        if self.quiz.still_has_questions() and self.quiz.question_number<10:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question,text="You have answered all the question!\n"
                                                      f"Your score is {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disable")
            self.wrong_button.config(state="disable")


    def click_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def click_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#00FF00")
        else:
            self.canvas.config(bg="#FF0000")
        self.window.after(1000,self.get_next_question)



