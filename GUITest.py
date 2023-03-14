import tkinter as tk
import csv
import random
import sys

class QuizApp:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []
        self.current_question_amount = 0
        self.load_questions()
        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.question_label = tk.Label(self.window, text=self.questions[self.current_question_amount]['question'], font=('Arial', 18))
        self.question_label.pack(pady=20)
        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.window, text="", font=('Arial', 14), width=45, command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.answer_buttons.append(button)
        self.load_answers()
        self.window.mainloop()

    def load_questions(self):
        with open(self.filename, newline='',) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.questions.append(row)
            random.shuffle(self.questions)

    def load_answers(self):
        answers = []
        answers.append(self.questions[self.current_question_amount]['answer'])
        answers.append(self.questions[self.current_question_amount]['decoy1'])
        answers.append(self.questions[self.current_question_amount]['decoy2'])
        answers.append(self.questions[self.current_question_amount]['decoy3'])
        random.shuffle(answers)
        for i in range(4):
            self.answer_buttons[i]['text'] = answers[i]

    def check_answer(self, index):
        if self.answer_buttons[index]['text'] == self.questions[self.current_question_amount]['answer']:
            self.current_question_amount += 1
            if self.current_question_amount < len(self.questions):
                self.question_label['text'] = self.questions[self.current_question_amount]['question']
                self.load_answers()
            else:
                self.window.destroy()
        else:
            self.answer_buttons[index]['text'] = "Wrong! Try again"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("The correct format is: python quiz.py <filename.csv>")
        sys.exit(1)
    QuizApp(sys.argv[1])