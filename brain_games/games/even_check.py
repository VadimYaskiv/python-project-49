import random


def game_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def quest_num_f():
    QUEST_NUM = random.randint(1, 1000)
    return QUEST_NUM


def quest_answ_pair():
    quest_num = quest_num_f()

    if quest_num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return quest_num, right_answer
