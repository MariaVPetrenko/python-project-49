import prompt
import random
import math


def instruction():
    return 'Find the greatest common divisor of given numbers.'


def expression():
    first_int = random.randint(1, 100)
    second_int = random.randint(1, 100)
    return f'{first_int} {second_int}'


def answer():
    while True:
        try:
            return int(prompt.string('Your answer: '))
        except ValueError:
            print("Please enter a number.")


def condition(expression, user_answer):
    split_expression = expression.split()
    result = math.gcd(int(split_expression[0]), int(split_expression[1]))
    return result - user_answer == 0


def right_condition(expression):
    split_expression = expression.split()
    result = math.gcd(int(split_expression[0]), int(split_expression[1]))
    return result


def right_answer_if_condition_is_true(expression):
    split_expression = expression.split()
    result = math.gcd(int(split_expression[0]), int(split_expression[1]))
    return result


def right_answer_if_condition_is_false(expression):
    split_expression = expression.split()
    result = math.gcd(int(split_expression[0]), int(split_expression[1]))
    return result
