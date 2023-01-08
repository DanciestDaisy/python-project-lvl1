#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        rnd_int = randint(1, 99)
        print(f'Question: {rnd_int}')
        answer = prompt.string('You answer: ')
        if rnd_int % 2 == 0:
            if answer == "yes":
                print('Correct!')
                counter += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        else:
            if answer == "no":
                print('Correct!')
                counter += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
    if counter == 3:
        print(f'Congratulations, {name}!')
