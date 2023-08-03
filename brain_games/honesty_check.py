import prompt
import random


def honesty_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    for i in range(3):
        number = random.randint(1, 1000000)
        print(f'Question: {number}')
        answer = str.lower(prompt.string('Your answer: '))
        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('Correct!')
            correct_count += 1
            if correct_count == 3:
                print(f'Congratulations, {name}!')
        else:
            if number % 2 == 0:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
