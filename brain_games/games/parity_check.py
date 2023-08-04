import prompt
import random


def instruction():
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    return instruction


def answer():
    answer = str.lower(prompt.string('Your answer: '))
    return answer


def expression():
    expression = random.randint(1, 1000000)
    return expression


def condition():
    condition = (expression % 2 == 0 and answer == 'yes') or (expression % 2 != 0 and answer == 'no')
    return condition


def right_condition():
    right_condition = (expression % 2 == 0)
    return right_condition
