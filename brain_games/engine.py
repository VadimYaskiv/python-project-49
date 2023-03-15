import prompt
from brain_games.greeting import greet
from brain_games.greeting import welcome_user
import brain_games.greeting


def game(gen_quest_num, gen_result, var_print):
    greet()
    welcome_user()
    print(var_print())

    counter = 0

    while counter < 3:
        quest_num = gen_quest_num()
        result = gen_result()

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
