import random
import prompt
import brain_games.greeting


def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        question_num = random.randint(1, 1000)

        if question_num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        print(f'Question: {question_num}')
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
