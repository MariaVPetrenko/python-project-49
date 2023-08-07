import prompt
import random


def instruction():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def answer():
    return str.lower(prompt.string('Your answer: '))


def expression():
    return random.randint(1, 1000000)


def condition(expression, user_answer):
    return (expression % 2 == 0 and user_answer == 'yes') or (expression % 2 != 0 and user_answer == 'no')


def right_condition(expression):
    return expression % 2 == 0


def right_answer_if_condition_is_true():
    return 'yes'


def right_answer_if_condition_is_false():
    return 'no'

