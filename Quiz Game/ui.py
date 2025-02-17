from operator import truediv
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.score = 0
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        false = PhotoImage(file="./images/false.png")
        true = PhotoImage(file="./images/true.png")

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=2, padx=20, pady=20, columnspan=2)

        self.score_label = Label(
            text=f"score: {self.score}", bg=THEME_COLOR, font=("Arial", 20, "italic"),
        )
        self.score_label.grid(column=1, row=0)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="test",
            fill = THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)

        self.button_true = Button(image=true, highlightbackground="white", command=self.check_answer_true)
        self.button_true.grid(column=0, row=3)

        self.button_false = Button(image=false, highlightbackground="white", command=self.check_answer_false)
        self.button_false.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def change_color_red(self):
        self.canvas.config(bg="red")

    def change_color_green(self):
        self.canvas.config(bg="green")

    def change_color_default(self):
        self.canvas.config(bg="white")

    def level_up(self):
        self.score += 1
        self.score_label.config(text=f"score: {self.score}")

    def give_feedback(self, is_right):
        self.change_color_default()
        if is_right:
            green_effect = self.window.after(0, self.change_color_green)
            self.level_up()
        else:
            red_effect = self.window.after(0, self.change_color_red)
        self.window.after(1000, self.change_color_default)
        self.window.after(1000, self.get_next_question)
