import prompt
import random


INSTRUCTION = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = []
    start = random.randint(1, 1000)
    step = random.randint(2, 9)
    stop = random.randint(start + step + 20, 1000)

    i = start
    while i < stop:
        progression.append(i)
        i += step
    progression = progression[:10]
    random_element_index = random.randint(1, len(progression) - 2)
    final_progression = progression.copy()
    final_progression[random_element_index] = '..'
    final_progression = " ".join(map(str, final_progression))
    question = f'Question: {final_progression}'
    progression = final_progression.split()
    dots_index = progression.index('..')
    step = (
        int(progression[dots_index + 1])
        - int(progression[dots_index - 1])
    ) / 2
    correct_answer = str(int(progression[dots_index - 1]) + int(step))
    return question, correct_answer
