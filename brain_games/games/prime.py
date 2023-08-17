import random


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    return k <= 0


def get_question_and_answer():
    current_expression = random.randint(2, 100)
    if is_prime(current_expression):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return current_expression, correct_answer
