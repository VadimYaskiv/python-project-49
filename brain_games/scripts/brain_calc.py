from brain_games.games.calc_check import var_print
from brain_games.games.calc_check import quest_result
from brain_games.engine import game

print('brain-calc\n')


def main():
    game(quest_result, var_print)


if __name__ == '__main__':
    main()
