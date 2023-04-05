import math
import random


def game_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


INTERVAL = (1, 100)


def quest_answ_pair():
    quest_num = random.randint(*INTERVAL)
    right_answer = 'yes' if is_prime(quest_num) else 'no'
    return quest_num, right_answer
