from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
import html
from ui import QuizUi

question_bank = []
recived = requests.get(
    url='https://opentdb.com/api.php?amount=10&category=24&difficulty=easy&type=boolean')
data = recived.json()
questions_base = [(i['question'], i['correct_answer'])
                  for i in data['results']]
for question in questions_base:
    question_text = html.unescape(question[0])
    question_answer = question[1]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)
quiz = QuizBrain(question_bank)
QuizUi(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
