import random


def var_print():
    return 'What number is missing in the progression?'


def members():
    start_num = random.randint(1, 11)
    end_num = random.randint(50, 70)
    step = random.randint(2, 10)
    return start_num, end_num, step


def str_progr():
    start_num, end_num, step = members()
    progr = list(range(start_num, end_num, step))
    change_num = random.choice(progr)
    progr[progr.index(change_num)] = '..'
    quest_num = ' '.join(map(str, progr))
    return change_num, quest_num


def quest_result():
    change_num, quest_num = str_progr()
    result = str(change_num)
    return quest_num, result
