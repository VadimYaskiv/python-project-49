import random


def game_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    else:
        return True


def quest_answ_pair():
    QUEST_NUM = random.randint(1, 100)

    if is_prime(QUEST_NUM):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return QUEST_NUM, right_answer
