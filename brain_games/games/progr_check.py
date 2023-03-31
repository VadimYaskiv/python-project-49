import random


def game_task():
    return 'What number is missing in the progression?'


INIT_TERM_INTERVAL = (1, 11)
FINAL_TERM_INTERVAL = (52, 70)
DIFF_INTERVAL = (2, 10)


def initial_term():
    initial_term = random.randint(*INIT_TERM_INTERVAL)
    return initial_term


def final_term():
    final_term = random.randint(*FINAL_TERM_INTERVAL)
    return final_term


def common_diff():
    common_diff = random.randint(*DIFF_INTERVAL)
    return common_diff


def make_progress(initial_term, final_term, common_diff):
    initial_term = initial_term()
    final_term = final_term()
    common_diff = common_diff()
    progr = list(range(initial_term, final_term, common_diff))
    return progr


def quest_answ_pair():
    progr = make_progress(initial_term, final_term, common_diff)
    change_index = random.randrange(len(progr))
    change_num = progr[change_index]
    progr[change_index] = '..'
    quest_num = ' '.join(map(str, progr))
    return quest_num, str(change_num)
