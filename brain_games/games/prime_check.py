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
    INTERVAL = (1, 100)
    quest_num = random.randint(INTERVAL[0], INTERVAL[1])

    if is_prime(quest_num):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return quest_num, right_answer
