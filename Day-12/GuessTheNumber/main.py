import random
import os
from art import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def start_game():
    global game_state
    game_state=True
    print(logo)
    global number_in_game
    number_in_game=generate_number()
    difficulty_level=input("Enter the Level of difficulty (hard/easy):")
    global lives
    if difficulty_level=='hard':
        lives=5
    else:
        lives=10

def restart_game():
    cls()
    start_game()

def stop_game():
    global game_state
    game_state=False

def generate_number():
    return random.randint(0,100)

start_game()

while(game_state):
    
    guessed_number=int(input("Guess The Number: "))
    
    if guessed_number>number_in_game and abs(guessed_number-number_in_game)>10:
        print("Guess Alot Lower")
        lives-=1
    elif guessed_number>number_in_game and abs(guessed_number-number_in_game)<=10:
        print("Guess A Little Lower")
        lives-=1
    elif guessed_number<number_in_game and abs(guessed_number-number_in_game)<=10:
        print("Guess A Little Higher")
        lives-=1
    elif guessed_number<number_in_game and abs(guessed_number-number_in_game)>10:
        print("Guess Alot Higher")
        lives-=1
    elif guessed_number==number_in_game:
        print(f"Your guess is spot on! You Win! with {lives} left!") 
    
    if lives==0:
        print("Lives over! You lose!")
        stop_game()
        