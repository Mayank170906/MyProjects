import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        def true():

            checking_answer = self.quiz.check_answer('True')
            score = self.quiz.score
            # self.feedback('True')
            self.label_score.config(text=f'Score:{score}')
            if checking_answer:
                self.canvas.config(background='green')
                self.window.update()
                self.window.after(1000)
                self.canvas.config(background='white')
            else:
                self.canvas.config(background='red')
                self.window.update()
                self.window.after(1000)
                self.canvas.config(background='white')
            if self.quiz.still_has_questions():
                self.next_q()
            else:
                self.canvas.itemconfig(self.question_text, text=score)
                self.button_true.config(state='disabled')
                self.button_false.config(state='disabled')

        def false():

            checking_answer = self.quiz.check_answer('False')
            # self.feedback('False')
            score = self.quiz.score
            self.label_score.config(text=f'Score:{score}')
            if checking_answer:
                self.canvas.config(background='green')
                self.window.update()
                self.window.after(1000)
                self.canvas.config(background='white')
            else:
                self.canvas.config(background='red')
                self.window.update()
                self.window.after(1000)
                self.canvas.config(background='white')
            if self.quiz.still_has_questions():
                self.next_q()
            else:
                self.canvas.itemconfig(self.question_text, text=score)
                self.button_false.config(state='disabled')
                self.button_true.config(state='disabled')

        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.label_score = tkinter.Label(
            text=f'Score={0}', highlightthickness=0, background=THEME_COLOR, foreground='white', pady=10)
        self.label_score.grid(row=0, column=1)
        self.canvas = tkinter.Canvas()
        self.canvas.config(width=300, height=250,
                           background='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text='Text', activefill='black',
                                                     font=('Arial', 12, 'italic'), width=140)
        self.false_img = tkinter.PhotoImage(file='./images/false.png')
        self.true_img = tkinter.PhotoImage(file='./images/true.png')
        self.button_true = tkinter.Button(image=self.true_img, command=true)
        self.button_false = tkinter.Button(image=self.false_img, command=false)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.next_q()
        self.window.mainloop()

    def next_q(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
