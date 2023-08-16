import random


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    current_expression = random.randint(2, 100)
    question = f'Question: {current_expression}'
    k = 0
    for i in range(2, current_expression // 2 + 1):
        if (current_expression % i == 0):
            k = k + 1
    k <= 0
    if k <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
