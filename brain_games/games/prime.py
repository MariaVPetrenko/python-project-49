import prompt
import random


def instruction():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def answer():
    return str.lower(prompt.string('Your answer: '))


def expression():
    return random.randint(2, 100)


def condition(expression, user_answer):
    k = 0
    for i in range(2, expression // 2 + 1):
        if (expression % i == 0):
            k = k + 1
    return (k <= 0 and user_answer == 'yes') or (k > 0 and user_answer == 'no')


def right_condition(expression):
    k = 0
    for i in range(2, expression // 2 + 1):
        if (expression % i == 0):
            k = k + 1
    return k <= 0


def right_answer_if_condition_is_true(expression):
    return 'yes'


def right_answer_if_condition_is_false(expression):
    return 'no'
