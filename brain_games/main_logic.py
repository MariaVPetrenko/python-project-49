import prompt


def launch_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INSTRUCTION)
    correct_count = 0
    NUMBER_OF_ROUNDS = 3
    for i in range(NUMBER_OF_ROUNDS):
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
                correct_answer = game.right_answer_if_condition_is_true(
                    current_expression)
            else:
                correct_answer = game.right_answer_if_condition_is_false(
                    current_expression)
            print(f"'{current_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
