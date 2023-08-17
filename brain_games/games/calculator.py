import random


INSTRUCTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def get_question_and_answer():
    EXPRESSION_OPERATOR = random.choice(OPERATORS)
    EXPRESSION_FIRST_NUMBER = random.randint(1, 100)
    EXPRESSION_SECOND_NUMBER = random.randint(1, 100)
    current_expression = (f'{EXPRESSION_FIRST_NUMBER} {EXPRESSION_OPERATOR} '
                         f'{EXPRESSION_SECOND_NUMBER}')
    if EXPRESSION_OPERATOR == '+':
        correct_answer = EXPRESSION_FIRST_NUMBER + EXPRESSION_SECOND_NUMBER
    elif EXPRESSION_OPERATOR == '-':
        correct_answer = EXPRESSION_FIRST_NUMBER - EXPRESSION_SECOND_NUMBER
    elif EXPRESSION_OPERATOR == '*':
        correct_answer = EXPRESSION_FIRST_NUMBER * EXPRESSION_SECOND_NUMBER
    correct_answer = str(eval(current_expression))
    return current_expression, correct_answer
