import prompt
from brain_games.greeting import greet
from brain_games.greeting import welcome_user
import brain_games.greeting


def game(quest_result, short_name, var_print):
    print(short_name())
    greet()
    welcome_user()
    print(var_print())

    counter = 0

    while counter < 3:
        quest_num, result = quest_result()

        print(f'Question: {quest_num}')
        answer = prompt.string('Your answer: ')

        if result == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {brain_games.greeting.name}!")
            break

        if counter == 2:
            print(f'Congratulations, {brain_games.greeting.name}!')

        counter += 1
