import prompt


def game(play_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(play_module.var_print())

    counter = 0

    while counter < 3:
        quest_num, result = play_module.quest_result()

        print(f'Question: {quest_num}')
        answer = prompt.string('Your answer: ')

        if result == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

        if counter == 2:
            print(f'Congratulations, {name}!')

        counter += 1
