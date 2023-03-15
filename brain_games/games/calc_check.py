import random


def var_print():
    return 'What is the result of the expression?'


def gen_quest_num():
    global operator
    global first_var
    global second_var
    first_var = random.randint(0, 10)
    second_var = random.randint(0, 10)
    operator = random.choice(['+', '-', '*'])
    quest_num = f'{first_var} {operator} {second_var}'
    return quest_num


def gen_result():
    if operator == '+':
        result = first_var + second_var
    elif operator == '-':
        result = first_var - second_var
    elif operator == '*':
        result = first_var * second_var
    return str(result)
