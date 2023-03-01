import random
import prompt
import brain_games.greeting


def game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        question_num = random.randint(1, 100)

        i = 2
        while i * i <= question_num:
            if question_num % i == 0:
                result = 'no'
                break
            i += 1
        else:
            result = 'yes'

        print(f"Question: {question_num}")
        answer = prompt.string('Your answer: ')

        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {brain_games.greeting.name}!")
            break

        if counter == 2:
            print(f'Congratulations, {brain_games.greeting.name}!')

        counter += 1
