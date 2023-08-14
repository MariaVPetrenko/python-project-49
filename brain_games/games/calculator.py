import prompt
import random


INSTRUCTION = 'What is the result of the expression?'


def expression():
    operators = ['+', '-', '*']
    first_int = random.randint(1, 100)
    operator = random.choice(operators)
    second_int = random.randint(1, 100)
    return f'{first_int} {operator} {second_int}'


def answer():
    while True:
        try:
            return int(prompt.string('Your answer: '))
        except ValueError:
            print("Please enter a number.")


def condition(expression, user_answer):
    result = eval(expression)
    return result - user_answer == 0


def right_condition(expression):
    result = eval(expression)
    return result


def right_answer_if_condition_is_true(expression):
    result = eval(expression)
    return result


def right_answer_if_condition_is_false(expression):
    result = eval(expression)
    return result
