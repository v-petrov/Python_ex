import time, random

print("\nHello and welcome to my mini-game 'Guess the number'.\nI hope you like it!\n")
print("Let's start with the rules!")
time.sleep(1)

def rules():
    global tries, score, counter, random_number
    random_number = random.randint(0, 100)
    counter = 0
    tries = 5
    score = 50
    print(f" 1) You have {tries} tries to guess the number.\n 2) Each time you guess it wrong your points are going down by 10: You start with 50 points. Good luck.\n")
    time.sleep(1)
    first_clue()

def game_loop():
    global loop, random_number
    loop = input("Do you want to have a go one more time?, y = yes, n = no: ")
    if loop != 'y' and loop != 'n':
        while loop != 'y' and loop != 'n':
            print('Nice try...')
            loop = input("Do you want to have a go one more time?, y = yes, n = no: ")
    if loop == 'y':
        random_number = random.randint(1, 100)
        print("The rules:")
        rules()
    elif loop == 'n':
        print("\nThank you for playing and see you again!")
        exit()

def comparing():
    global score, tries
    if random_number == num:
        print(f'\nCongratulations,you guessed the number [{random_number}] and you have won {score} points.')
        game_loop()
    else:
        score -= 10
        tries -= 1
        print(f"Sorry, you didn't get it quite right! Try again. You have {tries} tries remaining\n")
        if counter == 1:
            second_clue()
        elif counter == 2:
            third_clue()
        elif counter == 3:
            fourth_clue()
        elif counter == 4:
            fifth_clue()
    
    if tries == 0:
        print(f"Really???.....The number was {random_number}! :(")
        print(f"I'm sorry you don't have more attempts.")
        game_loop()

def first_clue():
    random_number_clue = 0
    for i in str(random_number):
        if i == '-':
            continue
        random_number_clue += 1
    print(f"First clue, length of the number: {random_number_clue} digit/s")
    time.sleep(1)
    number()

def number():
    global num, counter
    print(f"Available point for grabe: {score} points")
    while True:
        try:
            num = int(input('Guess the number: '))
        except ValueError:
            print('Please enter a valid number. Try again!')
        else:
            counter += 1
            time.sleep(1)
            comparing()
            break

def second_clue():
    if random_number % 2 == 0:
        print("Second clue, the number is even!")
    else:
        print("Second clue, the number is odd!")
    time.sleep(1)
    number()

def third_clue():
    for j in range(3, abs(random_number)+1):
        if random_number <= 9:
            print("I don't think you need that clue for THAT number, try without it!")
            break
        if random_number % j == 0:
            print(f"Third clue, the number can be divided by {j}")
            break
    time.sleep(1)
    number()

def fourth_clue():
    if random_number >= 1 and random_number <= 33:
        print("Fourth clue, the number is between [1,33]")
        time.sleep(1)
        number()
    elif random_number > 33 and random_number <= 66:
        print("Fourth clue, the number is between [34,66]")
        time.sleep(1)
        number()
    else:
        print("Fourth clue, the number is between [67,100]")
        time.sleep(1)
        number()

def fifth_clue():
    difference = abs(random_number - num)
    if difference >= 1 and difference <= 20:
        print("Fifth clue, the number is in range of 20 numbers of the last number you have entered.")
        time.sleep(1)
        number()
    else:
        print("Fifth clue, the number is at least 20 numbers of the last number you have entered.")
        time.sleep(1)
        number()

rules()