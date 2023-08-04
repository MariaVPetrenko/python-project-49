from brain_games import main_logic
from brain_games.games import parity_check
from brain_games.games.parity_check import instruction, answer, expression, condition, right_condition


def main():
     main_logic.main_logic(parity_check)

if __name__ == '__main__':
    
    main()
