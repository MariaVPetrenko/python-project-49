import prompt
import random


def instruction():
    return 'What number is missing in the progression?'


def expression():
    progression = []
    start = random.randint(1, 1000)
    step = random.randint(1, 9)
    stop = random.randint(start + step + 20, 1000)

    i = start
    while i < stop:
        progression.append(i)
        i += step
    progression = progression[:10]
    random_element_index = random.randint(1, len(progression) - 2)
    final_progression = progression.copy()
    final_progression[random_element_index] = '..'
    final_progression = " ".join(map(str,final_progression))
    return final_progression


def answer():
    while True:
        try:
            return int(prompt.string('Your answer: '))
        except ValueError:
            print("Please enter a number.")


def condition(expression, user_answer):
    progression = expression.split()
    dots_index = progression.index('..')
    step = (int(progression[dots_index + 1]) - int(progression[dots_index - 1])) / 2
    result = int(progression[dots_index - 1]) + int(step)
    return result - user_answer == 0


def right_condition(expression):
    progression = expression.split()
    dots_index = progression.index('..')
    step = (int(progression[dots_index + 1]) - int(progression[dots_index - 1])) / 2
    result = int(progression[dots_index - 1]) + int(step)
    return result


def right_answer_if_condition_is_true(expression):
    progression = expression.split()
    dots_index = progression.index('..')
    step = (int(progression[dots_index + 1]) - int(progression[dots_index - 1])) / 2
    result = int(progression[dots_index - 1]) + int(step)
    return result


def right_answer_if_condition_is_false(expression):
    progression = expression.split()
    dots_index = progression.index('..')
    step = (int(progression[dots_index + 1]) - int(progression[dots_index - 1])) / 2
    result = int(progression[dots_index - 1]) + int(step)
    return result
