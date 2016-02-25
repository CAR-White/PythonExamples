# This is a guess the number game.

import random
name = input('What is you name: ')
print('Hi ' + str(name) + ', I am thinking of a number between 1 and 20. ', end = "")

playAgain = 'y'
while playAgain == 'y':
    secretNumber = random.randint(1, 20)
    # Ask the player to guess 6 times.
    for guessesTaken in range(1, 7):
        print('Take a guess: ', end = "")
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
           break    # This condition is the correct guess!

    if guess == secretNumber:
        if guessesTaken == 1:
            guessesString = ' guess!'
        else:
            guessesString = ' guesses!'
        print('Good job! You guessed my number in ' + str(guessesTaken) + guessesString)
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

    playAgain = ''
    while (playAgain != 'y') and (playAgain != 'n'):
        playAgain = input('Would you like to play again? (y/n): ')

print('GoodBye')
