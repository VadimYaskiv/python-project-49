import random


def game_task():
    return 'What is the result of the expression?'


def quest_answ_pair():
    FIRST_VAR = random.randint(0, 10)
    SECOND_VAR = random.randint(0, 10)
    OPERATOR = random.choice(['+', '-', '*'])
    quest_num = f'{FIRST_VAR} {OPERATOR} {SECOND_VAR}'

    if OPERATOR == '+':
        right_answer = FIRST_VAR + SECOND_VAR
    elif OPERATOR == '-':
        right_answer = FIRST_VAR - SECOND_VAR
    elif OPERATOR == '*':
        right_answer = FIRST_VAR * SECOND_VAR

    return quest_num, str(right_answer)
