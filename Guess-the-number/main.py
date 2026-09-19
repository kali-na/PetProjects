import random

print(
    'Hi, my dear friend, this game is called “Guess the Number.”' \
'\nMy name is Monica.' \
'\nI"ll think of any number from 1 to 1000, and you have 15 attempts to guess my number.' \
'\nAre you ready?' \
'\n\nIf you"re ready, write “YES”'
)

approval_user = input('Write: ')

while True:

    if approval_user == 'YES':

        # number_bot = random.randint(1, 1000)
        number_bot = 500
        attempts_level1 = 1

        print('\nI"ve guessed the number!\nLevel 1.')

        while attempts_level1 < 16:

            try:
                number_user = int(input('Write number here: '))
            except ValueError:
                print('\nPlease write a number!')
                continue

            if number_user > number_bot:
                print(f'\nAttempts: {attempts_level1}')
                print('NO! Donw')
                attempts_level1 += 1
            if number_user < number_bot:
                print(f'\nAttempts: {attempts_level1}')
                print('No! UP')
                attempts_level1 += 1
            if number_user == number_bot:

                print('\nYEEEEP! You WIN.')
                print('\nA new level begins.\nLevel number 2.\nNow you have 10 attempts.')

                attempts_level2 = 1
                while attempts_level1 < 11:
                    try:
                        number_user2 = int(input('Write number here: '))
                    except ValueError:
                        print('\nPlease write a number!')
                        continue

                    if number_user2 > number_bot:
                        print(f'\nAttempts: {attempts_level2}')
                        print('NO! Donw')
                        attempts_level2 += 1
                    if number_user2 < number_bot:
                        print(f'\nAttempts: {attempts_level2}')
                        print('No! UP')
                        attempts_level2 += 1
                    if number_user2 == number_bot:
                        print('\nYEEEEP! You WIN.')
                        break

        else:
            print(f'\nThe attempts are over. It was guessed: {number_bot}')
            
    else:
        print('Error, please try again.')
        approval_user = input('Write: ')
