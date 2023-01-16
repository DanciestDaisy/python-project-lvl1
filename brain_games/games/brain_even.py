from random import randint
from brain_games.game_pattern import ans_que

condition = 'Answer "yes" if the number is even, otherwise answer "no".'


def main_game(name):
    rnd_int = randint(1, 99)
    question = rnd_int
    if rnd_int % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    err = ans_que(question, result, name)
    return err
