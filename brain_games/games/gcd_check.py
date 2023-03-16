import random
import math


def short_name():
    return 'brain-gcd\n'


def var_print():
    return 'Find the greatest common divisor of given numbers.'


def quest_result():
    first_div = random.randint(1, 30)
    second_div = random.randint(1, 30)
    quest_num = f'{first_div} {second_div}'

    result = math.gcd(first_div, second_div)

    return quest_num, str(result)
