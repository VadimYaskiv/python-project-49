import random


def game_task():
    return 'What number is missing in the progression?'


INIT_TERM_INTERVAL = (1, 11)
LENGTH_INTERVAL = (52, 70)
DIFF_INTERVAL = (2, 10)


def make_progress(initial_term, final_term, common_diff):
    return list(range(initial_term, final_term, common_diff))


def quest_answ_pair():
    initial_term = random.randint(*INIT_TERM_INTERVAL)
    length = random.randint(*LENGTH_INTERVAL)
    common_diff = random.randint(*DIFF_INTERVAL)

    progression = make_progress(initial_term, length, common_diff)
    change_index = random.randrange(len(progression))
    change_num = progression[change_index]
    progression[change_index] = '..'
    quest_num = ' '.join(map(str, progression))
    return quest_num, str(change_num)
