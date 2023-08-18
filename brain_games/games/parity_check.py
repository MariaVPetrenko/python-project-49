import random


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_START = 1
RANGE_FINISH = 1000000


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = random.randint(RANGE_START, RANGE_FINISH)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
