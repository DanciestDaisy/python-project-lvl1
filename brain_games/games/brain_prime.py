from random import randint
from brain_games.game_pattern import ans_que

condition = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def main_game(name):
    number = randint(3, 9)
    count = 0
    if number % 2 == 0:
        result = 'no'
    else:
        for i in range(3, number // 2 + 1):
            if number % i == 0:
                count += 1
        if count > 0:
            result = 'no'
        else:
            result = 'yes'
    question = f'{number}'
    err = ans_que(question, result, name)
    return err
