import random


INSTRUCTION = 'What is the result of the expression?'


def get_question_and_answer():
    operators = ['+', '-', '*']
    first_int = random.randint(1, 100)
    operator = random.choice(operators)
    second_int = random.randint(1, 100)
    current_expression = f'{first_int} {operator} {second_int}'
    question = f'Question: {current_expression}'
    correct_answer = str(eval(current_expression))
    return question, correct_answer
