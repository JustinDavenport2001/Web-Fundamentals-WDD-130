#08 Team Activity

word = 'commitment'

fav = input('What is your favorite letter? ')

for letter in word:
    if letter.lower() == fav.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")    
        
print('')