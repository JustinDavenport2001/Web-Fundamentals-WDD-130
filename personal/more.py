print("Welcome to Wordle!!")
word = "hello"
game = True
guess_count = 0
guess = -1


print('Your hint is: ', end="")
for i in range(len(word)):
    letter = word[i]
    print(f"_ ", end="")

while game == True:
    print("\nWhat is your guess? ", end='')     
    guess = input()
    print('Your hint is: ', end="")
    guess_count = guess_count + 1
    for i in range(len(guess)):
        if word[i] == guess[i].lower():
            print(guess[i].upper(), end ='')
        elif guess[i].lower() in word:
            print(guess[i].lower(), end='')
        elif guess[i].lower() not in word: 
            print("_ ", end ='')
        else: 
            print("error")
                
    if word == guess:
        game = False 
        print('')
        print('Congrats your guessed the word!!')
            
print(f'It took you {guess_count} guesses.')