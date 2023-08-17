import prompt


ROUNDS_COUNT = 3


def launch_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INSTRUCTION)
    for i in range(ROUNDS_COUNT):
        current_expression, correct_answer = game.get_question_and_answer()
        question = f'Question: {current_expression}'
        print(question)
        user_answer = str.lower(prompt.string('Your answer: '))
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
