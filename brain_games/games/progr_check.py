import random


def var_print():
    print('What number is missing in the progression?')


def gen_quest_num():
    global change_num
    start_num = random.randint(1, 11)
    end_num = random.randint(50, 70)
    step = random.randint(2, 10)
    progr = list(range(start_num, end_num, step))

    change_num = random.choice(progr)
    progr[progr.index(change_num)] = '..'

    quest_num = ' '.join(map(str, progr))
    return quest_num


def gen_result():
    result = str(change_num)
    return result
