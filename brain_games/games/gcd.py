import random
import math


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_int = random.randint(1, 100)
    second_int = random.randint(1, 100)
    current_expression = f'{first_int} {second_int}'
    question = f'Question: {current_expression}'
    correct_answer = str(math.gcd(first_int, second_int))
    return question, correct_answer
