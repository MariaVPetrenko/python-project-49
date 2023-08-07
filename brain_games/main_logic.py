import prompt
import random


def main_logic(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.instruction())
    correct_count = 0
    for i in range(3):
        current_expression = game.expression()
        print(f'Question: {current_expression}')
        current_answer = game.answer()
        if game.condition(current_expression, current_answer):
            print('Correct!')
            correct_count += 1
            if correct_count == 3:
                print(f'Congratulations, {name}!')
        else:
            if game.right_condition(current_expression):
                correct_answer = game.right_answer_if_condition_is_true()
            else:
                correct_answer = game.right_answer_if_condition_is_false()
            print(f"'{current_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
