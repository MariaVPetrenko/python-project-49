#!/usr/bin/env python3
from brain_games import main_logic
from brain_games.games import gcd


def main():
    main_logic.launch_game(gcd)


if __name__ == '__main__':

    main()
