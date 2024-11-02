#W07 Team Activity

import random

magic = random.randint(1,100)

guess = -1

while guess != magic:
    guess = int(input('What is your guess? '))
    if guess > magic:
        print('Lower')
    elif guess < magic:
        print('Higher')
    else:
        print('You guessed it!!')