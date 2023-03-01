import random
import prompt
import brain_games.greeting


def game():
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        start_num = random.randint(1, 11)
        end_num = random.randint(50, 70)
        step = random.randint(2, 10)
        progr = list(range(start_num, end_num, step))

        change_num = random.choice(progr)
        progr[progr.index(change_num)] = '..'
        print(f"Question: {', '.join(map(str, progr))}")
        answer = prompt.string('Your answer: ')

        if answer == str(change_num):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{change_num}'.")
            print(f"Let's try again, {brain_games.greeting.name}!")
            break
        if counter == 2:
            print(f'Congratulations, {brain_games.greeting.name}!')

        counter += 1
