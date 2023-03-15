import random


def var_print():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def gen_quest_num():
    global quest_num
    quest_num = random.randint(1, 1000)
    return quest_num


def gen_result():
    if quest_num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result
