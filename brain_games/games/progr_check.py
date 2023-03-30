import random


def game_task():
    return 'What number is missing in the progression?'


def progress():
    INIT = (1, 11)
    FINAL = (52, 70)
    DIFF = (2, 10)
    initial_term = random.randint(INIT[0], INIT[1])
    final_term = random.randint(FINAL[0], FINAL[1])
    common_diff = random.randint(DIFF[0], DIFF[1])
    progr = list(range(initial_term, final_term, common_diff))
    return progr


def quest_answ_pair():
    progr = progress()
    change_index = random.randrange(len(progr))
    change_num = progr[change_index]
    progr[change_index] = '..'
    quest_num = ' '.join(map(str, progr))
    return quest_num, str(change_num)
