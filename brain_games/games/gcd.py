import random
import math


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    EXPRESSION_FIRST_NUMBER = random.randint(1, 100)
    EXPRESSION_SECOND_NUMBER = random.randint(1, 100)
    current_expression = f'{EXPRESSION_FIRST_NUMBER} {EXPRESSION_SECOND_NUMBER}'
    correct_answer = str(math.gcd(EXPRESSION_FIRST_NUMBER, EXPRESSION_SECOND_NUMBER))
    return current_expression, correct_answer
