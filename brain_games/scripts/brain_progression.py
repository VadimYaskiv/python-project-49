from brain_games.games.progr_check import var_print
from brain_games.games.progr_check import gen_quest_num
from brain_games.games.progr_check import gen_result
from brain_games.engine import game


print('brain-progression\n')


def main():
    game(gen_quest_num, gen_result, var_print)


if __name__ == '__main__':
    main()
