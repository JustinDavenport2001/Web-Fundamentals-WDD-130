#07 Prove

word = ('mosiah')
guess_count = 0
guess = -1
print('Welcome to the word guessing game!! ')
print('')

number_of_letters = len(word)
print('Your hint is: ', end="")
for index in range(number_of_letters):
    letter = word[index]
    print(f"_ ", end="")


while guess != word:
    print('')
    guess = input('What is your guess? ')
    print('Your hint is: ', end="")
    guess_count = guess_count + 1
    for index in range(number_of_letters):
        #if letter.lower(guess[index]) == word[index]:
        print(guess[index].lower)
        if guess[index] is letter.lower in word[index]:
            print(letter.upper(word[index]), end="")
        elif guess is letter.lower in word:
            print(letter.lower, end="")
        else:
            print('_ ', end="")
        
    print('')
    if word == guess:
        print('Congradulations! you guessed it! ')
    else:
        print('Your guess was not correct. ')

print(f'It took you {guess_count} guesses.')
    
    #else:
        #print('Sorry, the guess must have the same number of letters as the secret word.')


#if the letter is here but not in the right place put it in lowercase
#if the letter is in the right spot then make it uppercase
#if the letter is wrong print "_"