from random import randint
from brain_games.game_pattern import ans_que

condition = 'Find the greatest common divisor of given numbers.'


def main_game(name):
    int_1 = randint(1, 99)
    int_2 = randint(1, 99)
    question = f'{int_1} {int_2}'
    while int_1 != int_2:
        if int_1 > int_2:
            int_1 -= int_2
        else:
            int_2 -= int_1
    err = ans_que(question, int_1, name)
    return err
