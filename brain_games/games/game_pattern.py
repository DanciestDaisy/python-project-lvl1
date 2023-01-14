import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def ans_que(question, result, name):
    print(f'Question: {question}')
    answer = prompt.integer('Your answer: ')
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
