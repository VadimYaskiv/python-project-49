import random
import math


def game_task():
    return 'Find the greatest common divisor of given numbers.'


def quest_answ_pair():
    FIRST_DIV = random.randint(1, 30)
    SECOND_DIV = random.randint(1, 30)
    quest_num = f'{FIRST_DIV} {SECOND_DIV}'

    right_answer = math.gcd(FIRST_DIV, SECOND_DIV)

    return quest_num, str(right_answer)
