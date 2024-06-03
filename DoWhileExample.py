from random import randint

# python does not support do-while statement.
# Instead we can use a while loop and the break statements to emulate a do..while loop.

MAX = 10
MIN = 0
attempts = 1 

random_num = randint(MIN, MAX)

while True:
    guess_num = int(input(f'Enter the number between {MAX} and {MIN}: '))

    if guess_num > random_num:
        print(f'Enter the smaller number')

    elif guess_num < random_num:
        print(f'Enter the bigger number')
    else:
        print(f'Ohho! {random_num} is correct number you guess the number in {attempts}')

    attempts += 1