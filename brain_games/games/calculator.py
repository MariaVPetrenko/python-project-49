import random


INSTRUCTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']
RANGE_START = 1
RANGE_FINISH = 100


def get_question_and_answer():
    expression_operator = random.choice(OPERATORS)
    expression_first_number = random.randint(RANGE_START, RANGE_FINISH)
    expression_second_number = random.randint(RANGE_START, RANGE_FINISH)
    question = (f'{expression_first_number} {expression_operator} '
                f'{expression_second_number}')
    if expression_operator == '+':
        correct_answer = str(expression_first_number + expression_second_number)
    elif expression_operator == '-':
        correct_answer = str(expression_first_number - expression_second_number)
    elif expression_operator == '*':
        correct_answer = str(expression_first_number * expression_second_number)
    return question, correct_answer
