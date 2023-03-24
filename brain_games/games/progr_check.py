import random


def game_task():
    return 'What number is missing in the progression?'


def members():
    INITIAL_TERM = random.randint(1, 11)
    FINAL_TERM = random.randint(52, 70)
    COMMON_DIFF = random.randint(2, 10)
    return INITIAL_TERM, FINAL_TERM, COMMON_DIFF


def str_progr():
    initial_term, final_term, common_diff = members()
    progr = list(range(initial_term, final_term, common_diff))
    change_num = random.choice(progr)
    progr[progr.index(change_num)] = '..'
    quest_num = ' '.join(map(str, progr))
    return change_num, quest_num


def quest_answ_pair():
    change_num, quest_num = str_progr()
    right_answer = str(change_num)
    return quest_num, right_answer
