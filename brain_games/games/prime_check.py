import random


def game_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def quest_num_f():
    QUEST_NUM = random.randint(1, 100)
    return QUEST_NUM


def quest_answ_pair():
    quest_num = quest_num_f()

    i = 2
    while i * i <= quest_num:
        if quest_num % i == 0:
            right_answer = 'no'
            break
        i += 1
    else:
        right_answer = 'yes'

    return quest_num, right_answer
