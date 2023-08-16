import prompt


def launch_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INSTRUCTION)
    correct_count = 0
    NUMBER_OF_ROUNDS = 3
    for i in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_answer()
        current_expression = question
        print(f'Question: {current_expression}')
        user_answer = str.lower(prompt.string('Your answer: '))
        if user_answer == correct_answer:
            print('Correct!')
            correct_count += 1
            if correct_count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
