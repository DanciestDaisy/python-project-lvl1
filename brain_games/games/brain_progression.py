from random import randint
from brain_games.game_pattern import ans_que

condition = 'What number is missing in the progression?'


def main_game(name):
    first_int = randint(1, 100)
    diff = randint(1, 10)
    k = randint(5, 16)
    progression = [first_int + i*diff for i in range(k)]
    rnd_member = randint(1, k - 1)
    result = progression.pop(rnd_member)
    progression.insert(rnd_member, '..')
    question = f'{progression}'
    err = ans_que(question, result, name)
    return err
