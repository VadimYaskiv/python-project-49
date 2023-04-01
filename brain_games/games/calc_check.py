import random


def game_task():
    return 'What is the result of the expression?'


INTERVAL = (0, 10)


def first_second_var():
    return random.randint(*INTERVAL)


def operator_choice():
    return random.choice(['+', '-', '*'])


def quest_answ_pair():
    first_var = first_second_var()
    second_var = first_second_var()
    operator = operator_choice()
    quest_num = f'{first_var} {operator} {second_var}'

    if operator == '+':
        right_answer = first_var + second_var
    elif operator == '-':
        right_answer = first_var - second_var
    elif operator == '*':
        right_answer = first_var * second_var

    return quest_num, str(right_answer)
