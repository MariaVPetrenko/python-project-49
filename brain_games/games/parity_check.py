import random


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    current_expression = random.randint(1, 1000000)
    if is_even(current_expression):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return current_expression, correct_answer
