import random


def var_print():
    return 'What number is missing in the progression?'


def quest_result():
    start_num = random.randint(1, 11)
    end_num = random.randint(50, 70)
    step = random.randint(2, 10)
    progr = list(range(start_num, end_num, step))

    change_num = random.choice(progr)
    progr[progr.index(change_num)] = '..'

    quest_num = ' '.join(map(str, progr))

    result = str(change_num)

    return quest_num, result
