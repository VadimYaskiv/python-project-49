import random
import prompt
import math
import brain_games.greeting


def game():
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        first_div = random.randint(1, 30)
        second_div = random.randint(1, 30)
        print(f'Question: {first_div, second_div}')
        answer = prompt.string('Your answer: ')
        result = math.gcd(first_div, second_div)
        if answer == str(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {brain_games.greeting.name}!")
            break
        if counter == 2:
            print(f'Congratulations, {brain_games.greeting.name}!')

        counter += 1
