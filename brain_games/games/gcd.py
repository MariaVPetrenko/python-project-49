import random
import math


INSTRUCTION = 'Find the greatest common divisor of given numbers.'
RANGE_START = 1
RANGE_FINISH = 100


def get_question_and_answer():
    expression_first_number = random.randint(RANGE_START, RANGE_FINISH)
    expression_second_number = random.randint(RANGE_START, RANGE_FINISH)
    question = f'{expression_first_number} {expression_second_number}'
    correct_answer = str(math.gcd(expression_first_number,
                                  expression_second_number))
    return question, correct_answer
