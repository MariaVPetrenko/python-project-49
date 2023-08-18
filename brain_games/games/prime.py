import random


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_START = 1
RANGE_FINISH = 100


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(RANGE_START, RANGE_FINISH)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
