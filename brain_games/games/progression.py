import random


INSTRUCTION = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = []
    start = random.randint(1, 1000)
    step = random.randint(2, 9)
    length = random.randint(5, 10)

    i = start
    while len(progression) < length:
        progression.append(i)
        i += step
    random_element_index = random.randint(1, len(progression) - 2)
    progression[random_element_index] = '..'
    current_expression = " ".join(map(str, progression))
    progression = current_expression.split()
    dots_index = progression.index('..')
    step = (
        int(progression[dots_index + 1])
        - int(progression[dots_index - 1])
    ) / 2
    correct_answer = str(int(progression[dots_index - 1]) + int(step))
    return current_expression, correct_answer
