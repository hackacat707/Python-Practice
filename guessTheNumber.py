import random
secretNumber = random.randint(1, 20)
print ('Welcome to guess the number. I will think of a number between 1 and 20.')
for guessesTaken in range(1, 7):
    print('Guess the number: ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low, try higher')
    elif guess > secretNumber:
        print ('Your guess is too high, try lower')
    else:
        break

if guess == secretNumber:
    print ('Great, you guessed the number!')
else:
    print('Sorry, you didnt guess the number. The number was ' +str(secretNumber))
    
