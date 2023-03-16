from brain_games.games.calc_check import short_name
from brain_games.games.calc_check import var_print
from brain_games.games.calc_check import quest_result
from brain_games.engine import game


def main():
    game(quest_result, short_name, var_print)


if __name__ == '__main__':
    main()
