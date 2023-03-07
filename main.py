from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

question_bank = []


def create_list_of_questions(data):
    for question in data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


create_list_of_questions(question_data)
quiz = Quiz_brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

