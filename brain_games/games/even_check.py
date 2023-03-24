import random


def var_print():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def quest_num_f():
    quest_num = random.randint(1, 1000)
    return quest_num


def quest_result():
    quest_num = quest_num_f() 

    if quest_num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    return quest_num, result
