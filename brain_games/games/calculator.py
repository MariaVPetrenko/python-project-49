import random


INSTRUCTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']
RANGE_START = 1
RANGE_FINISH = 100


def get_question_and_answer():
    operator = random.choice(OPERATORS)
    first_number = random.randint(RANGE_START, RANGE_FINISH)
    second_number = random.randint(RANGE_START, RANGE_FINISH)
    question = (f'{first_number} {operator} {second_number}')
    if operator == '+':
        correct_answer = str(first_number + second_number)
    elif operator == '-':
        correct_answer = str(first_number - second_number)
    elif operator == '*':
        correct_answer = str(first_number * second_number)
    return question, correct_answer
