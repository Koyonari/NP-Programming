#An Yong Shyan, S10258126B

import random
print('Welcome to the Number Guessing Game')

#Generate random number
randomNumber = random.randint(1,100)

#Prompt user to guess number
guess = int(input('Try 1: Enter a number between 1 and 100 (or -1 to end): '))

#Check if guess is correct
tries = 1

while guess != -1 and tries != 5 and guess != randomNumber:
    if guess > randomNumber:
        tries += 1
        print(guess, 'is too high.')
        guess = int(input('Try ' + str(tries)+ ': Enter a number between 1 and 100 (or -1 to end): '))
    elif guess < randomNumber:
        tries += 1
        print(guess, 'is too low.')
        guess = int(input('Try ' + str(tries) + ':Enter a number between 1 and 100 (or -1 to end): '))

#When user has guessed correctly, 5 times or ended the game
if guess == randomNumber:
    print("Bingo!, you've got it right!")
elif tries >= 5:
    print('You were not able to guess the number in 5 tries. The number was ' + str(randomNumber) + '.')
elif guess == -1:
    print('You have ended the game. The number was ' + str(randomNumber) + '.')

print('Bye-bye!')
