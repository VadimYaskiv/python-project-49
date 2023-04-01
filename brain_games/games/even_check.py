import random


def game_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


INTERVAL = (0, 1000)


def quest_num_func():
    return random.randint(*INTERVAL)


def quest_answ_pair():
    quest_num = quest_num_func()
    right_answer = 'yes' if is_even(quest_num) else 'no'
    return quest_num, right_answer
