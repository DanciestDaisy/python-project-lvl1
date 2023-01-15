#!/usr/bin/env python3
import prompt
from brain_games.games.brain_gcd import main_game, condition


def main():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(condition)
    count = 0
    for _ in range(3):
        err = main_game(name)
        count += 1
        if err is True:
            count -= 1
            break
    if count == 3:
        print(f'Congratulations, {name}!')
