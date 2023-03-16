import random
import math


def var_print():
    return 'Find the greatest common divisor of given numbers.'


def quest_result():
    global first_div
    global second_div
    first_div = random.randint(1, 30)
    second_div = random.randint(1, 30)
    quest_num = f'{first_div} {second_div}'

    result = math.gcd(first_div, second_div)

    return quest_num, str(result)
