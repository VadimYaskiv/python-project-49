import random


def game_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def quest_answ_pair():
    QUEST_NUM = random.randint(1, 1000)

    if is_even(QUEST_NUM):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return QUEST_NUM, right_answer
