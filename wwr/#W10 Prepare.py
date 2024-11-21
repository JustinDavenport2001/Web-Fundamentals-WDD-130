#W10 Prepare

item = 0
items = []

print('Please enter the items of the shopping list (type: quit to finish)')

while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        items.append(item)          
            
print('\nThe shopping list is: ')   
for item in items:
    print(item)
    
print('\nThe Shopping list with indexes is:')
for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item}')
    
print()
index = int(input('Which item would you like to change? '))
new = input('What ist the new item? ')

items[index] = new

for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item}')