from brain_games.greeting import greet
from brain_games.greeting import welcome_user
from brain_games.games.calc_check import var_print
from brain_games.games.calc_check import gen_quest_num
from brain_games.games.calc_check import gen_result
from brain_games.engine import game

print('brain-calc\n')


def main():
    greet()
    welcome_user()
    var_print()
    game(gen_quest_num, gen_result)


if __name__ == '__main__':
    main()
