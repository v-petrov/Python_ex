import time, random

print("\nHello and welcome to my mini-game 'Rock-Paper-Scissors'.\nI hope you like it!\n")
time.sleep(1)

def games():
    global times, your_points, AI_points, played_times
    played_times = 0
    your_points = 0
    AI_points = 0
    while True:
        try:
            times = int(input('How many times would you like to play: '))
        except ValueError:
            print("Only whole numbers...\n")
        else:
            try:
                if times <= 0:
                    raise ValueError
            except ValueError:
                print("Only whole positive numbers...\n")
            else:
                print(f"Okey, {times} it is.")
                break
    time.sleep(1)
    your_chose()

def game_loop():
    global loop
    loop = input("Do you want to have a go one more time?, y = yes, n = no: ")
    if loop != 'y' and loop != 'n':
        while loop != 'y' and loop != 'n':
            print('Nice try...but only [y] or [n]')
            loop = input("Do you want to have a go one more time?, y = yes, n = no: ")
    if loop == 'y':
        print("Okey, we go again.\n")
        time.sleep(1)
        games()
    elif loop == 'n':
        print("\nThank you for playing and see you again!")
        exit()

def check():
    global played_times
    played_times += 1
    if played_times != times:
        time.sleep(1)
        your_chose()
    else:
        if your_points > AI_points:
            print(f"Congratulations, you have defeated the AI:\n Your score: {your_points}\n AI score: {AI_points}")
            time.sleep(1)
            game_loop()
        elif your_points < AI_points:
            print(f"I'm sorry, you have been defeated by the AI:\n Your score: {your_points}\n AI score: {AI_points}")
            time.sleep(1)
            game_loop()
        else:
            print(f"Good game, good game it's a tie:\n Your score: {your_points}\n AI score: {AI_points}")
            time.sleep(1)
            game_loop()

def your_chose():
    global rps
    rps = input("\nChoose: Rock, Paper or Scissors: ")
    while rps not in ['Rock','Paper','Scissors']:
        print('Sorry we expect only: Rock, Paper or Scissors\n')
        rps = input("Choose: Rock, Paper or Scissors: ")
    time.sleep(1)
    AI_chose()

def AI_chose():
    global chose
    list_rps = ['Rock', 'Paper', 'Scissors']
    chose = random.choice(list_rps)
    print(f'You are playing against: {chose}')
    time.sleep(1)
    result()

def result():
    global your_points, AI_points
    if rps == 'Rock' and chose == 'Scissors':
        print(f"\nBravo, you won: {rps} > {chose}")
        your_points += 1
        time.sleep(1)
        check()
    elif rps == 'Paper' and chose == 'Rock':
        print(f"\nBravo, you won: {rps} > {chose}")
        your_points += 1
        time.sleep(1)
        check()
    elif rps == 'Scissors' and chose == 'Paper':
        print(f"\nBravo, you won: {rps} > {chose}")
        your_points += 1
        time.sleep(1)
        check()

    elif rps == 'Rock' and chose == 'Paper':
        print(f"\nI'm sorry, you lost: {rps} < {chose}")
        AI_points += 1
        time.sleep(1)
        check()
    elif rps == 'Paper' and chose == 'Scissors':
        print(f"\nI'm sorry, you lost: {rps} < {chose}")
        AI_points += 1
        time.sleep(1)
        check()
    elif rps == 'Scissors' and chose == 'Rock':
        print(f"I'm sorry, you lost: {rps} < {chose}")
        AI_points += 1
        time.sleep(1)
        check()

    elif rps == 'Scissors' and chose == 'Scissors' or rps == "Paper" and chose == "Paper" or rps == "Rock" and chose == "Rock":
        print(f"\nThat's a tie: {rps} = {chose}")
        time.sleep(1)
        check()
    
    if your_points > AI_points:
        print(f"Congratulations, you have defeated the AI:\n Your score: {your_points}\nAI score: {AI_points}")
    elif your_points < AI_points:
        print(f"I'm sorry, you have been defeated by the AI:\n Your score: {your_points}\nAI score: {AI_points}")
    else:
        print(f"Good game, good game it's a tie:\n Your score: {your_points}\nAI score: {AI_points}")

games()