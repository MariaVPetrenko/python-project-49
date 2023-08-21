import random
import math


INSTRUCTION = 'Find the greatest common divisor of given numbers.'
RANGE_START = 1
RANGE_FINISH = 100


def get_question_and_answer():
    first_number = random.randint(RANGE_START, RANGE_FINISH)
    second_number = random.randint(RANGE_START, RANGE_FINISH)
    question = f'{first_number} {second_number}'
    correct_answer = str(math.gcd(first_number, second_number))
    return question, correct_answer
