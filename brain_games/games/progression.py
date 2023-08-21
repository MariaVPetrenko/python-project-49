import random


INSTRUCTION = 'What number is missing in the progression?'
START_RANGE_START = 1
START_RANGE_FINISH = 1000
STEP_RANGE_START = 2
STEP_RANGE_FINISH = 9
LEN_RANGE_START = 5
LEN_RANGE_FINISH = 10
INDEX_RANGE_START = 0


def create_progression(start, step, length):
    progression = []
    for i in range(start, start + step * length, step):
        progression.append(i)
    return progression


def get_question_and_answer():
    start = random.randint(START_RANGE_START, START_RANGE_FINISH)
    step = random.randint(STEP_RANGE_START, STEP_RANGE_FINISH)
    length = random.randint(LEN_RANGE_START, LEN_RANGE_FINISH)

    progression = create_progression(start, step, length)
    random_element_index = random.randint(INDEX_RANGE_START,
                                          len(progression) - 1)
    random_element = progression[random_element_index]
    progression[random_element_index] = '..'
    question = ' '.join(map(str, progression))
    correct_answer = str(random_element)
    return question, correct_answer
