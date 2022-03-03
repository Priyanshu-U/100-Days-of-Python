import random
import time
import random
import os
import art
import data


def cls():
    os.system('cls' if os.system == 'nt' else 'clear')


def reset():
    cls()
    global score
    score = 0


def play_again():
    j = input("Would you like to play again? (y/n)")
    if j == 'y':
        reset()
    else:
        global game_flag
        game_flag = False


def correct_answer(RC1, RC2):
    fa = RC1['follower_count']
    fb = RC2['follower_count']
    if fb > fa:
        return 'b'
    elif fa > fb:
        return 'a'
    else:
        return 0


game_flag = True
score = 0
while(game_flag):
    print(art.logo)
    print(f"Your score is {score}\n")
    RC1 = random.choice(data.data)
    i = data.data.index(RC1)
    RC2 = random.choice(data.data[:i]+data.data[i+1:])

    print(
        f"Compare the number of followers of\n\na){RC1['name']} a {RC1['description']} from {RC1['country']}{art.vs}\nb){RC2['name']} a {RC2['description']} from {RC2['country']}")
    user_choice = input("\nInput your choice? (a/b): ")

    if user_choice == correct_answer(RC1, RC2) or correct_answer(RC1, RC2) == 0:
        print("Correct Guess!")
        time.sleep(1)
        score += 1
        cls()
    else:
        cls()
        print(art.logo)
        print("Wrong Guess You Lose!")
        print(f"Your final score is {score}")
        play_again()
