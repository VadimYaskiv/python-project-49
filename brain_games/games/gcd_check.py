import random
import math


def var_print():
    print('Find the greatest common divisor of given numbers.')


def gen_quest_num():
    global first_div
    global second_div
    first_div = random.randint(1, 30)
    second_div = random.randint(1, 30)
    quest_num = f'Question: {first_div, second_div}'
    return quest_num


def gen_result():
    result = math.gcd(first_div, second_div)
    return str(result)
