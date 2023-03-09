import random


def var_print():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def gen_quest_num():
    global quest_num
    quest_num = random.randint(1, 100)
    return quest_num


def gen_result():
    i = 2
    while i * i <= quest_num:
        if quest_num % i == 0:
            result = 'no'
            break
        i += 1
    else:
        result = 'yes'

    return result
