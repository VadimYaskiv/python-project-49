import random


def game_task():
    return 'What number is missing in the progression?'


def progress():
    INITIAL_TERM = random.randint(1, 11)
    FINAL_TERM = random.randint(52, 70)
    COMMON_DIFF = random.randint(2, 10)
    progr = list(range(INITIAL_TERM, FINAL_TERM, COMMON_DIFF))
    return progr


def quest_answ_pair():
    progr = progress()
    change_num = random.choice(progr)
    progr[progr.index(change_num)] = '..'
    quest_num = ' '.join(map(str, progr))
    return quest_num, str(change_num)
