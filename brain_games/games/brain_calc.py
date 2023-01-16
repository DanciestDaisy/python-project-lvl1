from random import randint, choice
from brain_games.game_pattern import ans_que

condition = 'What is the result of the expression?'


def main_game(name):
    operation = choice(('+', '*', '-'))
    int_1 = randint(1, 99)
    int_2 = randint(1, 99)
    question = f'{int_1} {operation} {int_2}'
    result = None
    if operation == '+':
        result = int_1 + int_2
    elif operation == '*':
        result = int_1 * int_2
    elif operation == '-':
        result = int_1 - int_2
    else:
        print('operation error')
    if result is None:
        print('result error')
    err = ans_que(question, result, name)
    return err
