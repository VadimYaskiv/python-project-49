import random


def game_task():
    return 'What is the result of the expression?'


INTERVAL = (0, 10)


def quest_answ_pair():
    first_var = random.randint(*INTERVAL)
    second_var = random.randint(*INTERVAL)
    operator = random.choice(['+', '-', '*'])
    quest_num = f'{first_var} {operator} {second_var}'

    if operator == '+':
        right_answer = first_var + second_var
    elif operator == '-':
        right_answer = first_var - second_var
    elif operator == '*':
        right_answer = first_var * second_var

    return quest_num, str(right_answer)
