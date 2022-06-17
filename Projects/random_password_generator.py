import random

list_of_words = list()
list_of_elements = list()
while True:
    try:
        iterator = int(input('\nIterator of words, phrases or anything: '))
    except ValueError:
        print('You have to enter an integer...')
    else:
        try:
            if iterator <= 0:
                raise ValueError
        except ValueError:
            print('You have to enter a positive integer...')
        else: 
            for i in range(1, iterator+1):
                word = input(f'\nEnter a word, phrase or anything({i}): ')
                list_of_words.append(word)
            break

for w in list_of_words:
    for o in w:
        list_of_elements.append(o)

while True:
    try:
        length = int(input('\nHow long do you want your password to be: '))
    except ValueError:
        print('You have to enter an integer...')
    else:
        try:
            if length <= 0:
                raise ValueError
        except ValueError:
            print('You have to enter a positive integer...')
        else: 
            break

password = ''
for el in range(length):
    password += random.choice(list_of_elements)

with open('password.txt', 'a') as password_file:
    password_file.write(f"Your password is ready: {password}\n")