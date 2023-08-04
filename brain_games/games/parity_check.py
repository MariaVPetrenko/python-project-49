import prompt
import random


def parity_check():
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    answer = str.lower(prompt.string('Your answer: '))
    expression = random.randint(1, 1000000)
    condition = (expression % 2 == 0 and answer == 'yes') or (expression % 2 != 0 and answer == 'no')
    right_condition = (expression % 2 == 0)

    return instruction, answer, expression, condition, right_condition
