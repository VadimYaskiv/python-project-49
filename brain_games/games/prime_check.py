import random


def short_name():
    return 'brain-prime\n'


def var_print():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def quest_result():
    quest_num = random.randint(1, 100)

    i = 2
    while i * i <= quest_num:
        if quest_num % i == 0:
            result = 'no'
            break
        i += 1
    else:
        result = 'yes'

    return quest_num, result
