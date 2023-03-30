import random


def game_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def quest_answ_pair():
    INTERVAL = (0, 1000)
    quest_num = random.randint(INTERVAL[0], INTERVAL[1])

    if is_even(quest_num):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return quest_num, right_answer
