def ans_que(question, result, name):
    print(f'Question: {question}')
    answer = input('Your answer: ')
    if answer == result:
        print('Correct')
        err = False
        return err
    else:
        error(answer, result, name)
        err = True
        return err


def error(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
    print(f"Let's try again, {name}!")
