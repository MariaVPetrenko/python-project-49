import random


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    current_expression = random.randint(1, 1000000)
    question = f'Question: {current_expression}'
    if current_expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
