import prompt
import random


def main_logic(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(instruction)
    correct_count = 0
    for i in range(3):
        print(f'Question: {expression}')
        answer
        if condition:
            print('Correct!')
            correct_count += 1
            if correct_count == 3:
                print(f'Congratulations, {name}!')
        else:
            if right_condition:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
