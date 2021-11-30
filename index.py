import random
import time

def loginsystem():
    print("Welcome to the dice game!")
    time.sleep(1)
    for i in range(3, 0, -1):
        uone = input("Player 1, please enter your username: ")
        pone = input("Player 1, please enter your password: ")
        if uone == "adam" and pone == "apple":
            break
        else:
            print("Unknown credentials, please try again!")
    if i == 1:
        print("You've been locked out! Please try again later!")
        time.sleep(3)

    else:
        print("Player 1 has logged in!")
        time.sleep(2)
        for i in range(3, 0, -1):
            utwo = input("Player 2, please enter your username: ")
            ptwo = input("Player 2, please enter your password: ")
            if utwo == "george" and ptwo == "orange":
                break
            else:
                print("Unkown credentials, please try again!")
        if i == 1:
            print("You've been locked out, please try again later!")
            time.sleep(3)
        else:
            print("Player 2 has logged in!")
            time.sleep(2)
            print("There will be 5 rounds in this game")
            time.sleep(1)
            print("Each player gets to roll 2 dices in each round, if the sum of the 2 dices rolled is an equal number the player gains")
            time.sleep(3)
            ### End of login system ###


def roll():
    points = 0
    dice_one = random.randint(0, 6)
    dice_two = random.randint(0, 6)


    dice_total = dice_one + dice_two
    points = dice_total + points
    if dice_total % 2 == 0:
        points = points + 10
    else:
        points = points - 5
    return points


def dice_roll():
    score_one = 0
    score_two = 0   
    for i in range(1, 5):
        score_one += roll()
        print(f'In this round, player 1 has {score_one} points.')
        time.sleep(1)
        score_two += roll()
        print(f'In this round, player 2 has {score_two} points.')
        time.sleep(1)
    if score_one > score_two:
        print(f"Well done player 1! You won with a score of {score_one}")
        statement = str("Player 2 had a score of", score_one)
        f = open("scoreboard.txt", "a")
        f.write(statement)
    elif score_two > score_one:
        print(f"Well done player 2! You won with a score of {score_two}")
        ustatement = str("Player 2 had a score of", score_two)
        f = open("scoreboard.txt", "a")
        f.write(ustatement)
    else:
        print("Tie game!")



loginsystem()
roll()
dice_roll()