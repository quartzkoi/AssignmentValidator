import tkinter as tk
import csv
import random
import sys

class QuizApp:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []
        self.current_question_index = 0
        self.load_questions()
        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.question_label = tk.Label(self.window, text=self.questions[self.current_question_index]['question'], font=('Arial', 16))
        self.question_label.pack(pady=20)
        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.window, text="", font=('Arial', 12), width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.answer_buttons.append(button)
        self.load_answers()
        self.window.mainloop()

    def load_questions(self):
        with open(self.filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.questions.append(row)
            random.shuffle(self.questions)

    def load_answers(self):
        answers = []
        answers.append(self.questions[self.current_question_index]['answer'])
        answers.append(self.questions[self.current_question_index]['decoy1'])
        answers.append(self.questions[self.current_question_index]['decoy2'])
        answers.append(self.questions[self.current_question_index]['decoy3'])
        random.shuffle(answers)
        for i in range(4):
            self.answer_buttons[i]['text'] = answers[i]

    def check_answer(self, index):
        if self.answer_buttons[index]['text'] == self.questions[self.current_question_index]['answer']:
            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                self.question_label['text'] = self.questions[self.current_question_index]['question']
                self.load_answers()
            else:
                self.window.destroy()
        else:
            self.answer_buttons[index]['text'] = "Wrong Answer"
            self.answer_buttons[index]['state'] = 'disabled'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quiz.py <filename.csv>")
        sys.exit(1)
    QuizApp(sys.argv[1])