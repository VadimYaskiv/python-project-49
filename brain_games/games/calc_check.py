import random


def game_task():
    return 'What is the result of the expression?'


def quest_answ_pair():
    INTERVAL = (0, 10)
    first_var = random.randint(INTERVAL[0], INTERVAL[1])
    second_var = random.randint(INTERVAL[0], INTERVAL[1])
    operator = random.choice(['+', '-', '*'])
    quest_num = f'{first_var} {operator} {second_var}'

    if operator == '+':
        right_answer = first_var + second_var
    elif operator == '-':
        right_answer = first_var - second_var
    elif operator == '*':
        right_answer = first_var * second_var

    return quest_num, str(right_answer)
