import random
import math


def game_task():
    return 'Find the greatest common divisor of given numbers.'


INTERVAL = (0, 30)


def quest_answ_pair():
    first_div = random.randint(*INTERVAL)
    second_div = random.randint(*INTERVAL)
    quest_num = f'{first_div} {second_div}'

    right_answer = math.gcd(first_div, second_div)

    return quest_num, str(right_answer)
