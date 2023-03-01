import random
import prompt
import brain_games.greeting


def game():
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        first_var = random.randint(0, 10)
        second_var = random.randint(0, 10)
        operator = random.choice(['+', '-', '*'])
        print(f'Question: {first_var} {operator} {second_var}')
        answer = prompt.string('Your answer: ')
        if operator == '+':
            result = first_var + second_var
        elif operator == '-':
            result = first_var - second_var
        elif operator == '*':
            result = first_var * second_var
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
