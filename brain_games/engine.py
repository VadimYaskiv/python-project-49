import prompt


def play(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_module.game_task())

    NUM_OF_ROUNDS = 0

    while NUM_OF_ROUNDS < 3:
        quest_num, right_answer = game_module.quest_answ_pair()

        print(f'Question: {quest_num}')
        answer = prompt.string('Your answer: ')

        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break

        if NUM_OF_ROUNDS == 2:
            print(f'Congratulations, {name}!')

        NUM_OF_ROUNDS += 1
