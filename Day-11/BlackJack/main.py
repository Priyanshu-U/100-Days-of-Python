############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from pickle import NONE
import random
import os
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def player_scores(player_state_passed):
    player_score = sum(player_state_passed)
    if player_score > 21 and 11 in player_state_passed:
        index = player_state_passed.index(11)
        player_state_passed[index] = 1
        return player_scores(player_state_passed)
    else:
        return player_score


def draw():
    return random.choice(cards)


def restart():
    restart_flag = input("Would you like to play again? (y/n)")
    global game_flag   
    if restart_flag == 'y':
        start_game()
        game_flag= True
        cls()
    else:
        game_flag= False


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():
    global dealer_state
    dealer_state = []
    global player_state
    player_state = []

    for i in range(2):
        dealer_state.append(draw())
        player_state.append(draw())


global game_flag
game_flag = True
start_game()
while(game_flag):
    player = player_scores(player_state)
    dealer = player_scores(dealer_state)
    if sum(dealer_state) == 21:
        print("The Dealer is at 21 they win!")
        restart()

    elif sum(player_state) == 21:
        print("You win!")
        print(f"Your summation is {player} \n")
        restart()

    elif player_scores(player_state) > 21:
        print(f"Your summation is {player} \n")
        print("Dealer Wins!")
        restart()

    if game_flag==False:
        break
    player = player_scores(player_state)
    dealer = player_scores(dealer_state)
    print(f"The Dealer's first card is {dealer_state[0]}")

    print(f"Your summation is {player} \n")

    draw_state = input("Would you like to draw? (y/n)")

    if draw_state == 'y':
        player_state.append(draw())
    elif draw_state == 'n':
        while(dealer < 17):
            dealer_state.append(draw())
            dealer = player_scores(dealer_state)
        player = player_scores(player_state)
        dealer = player_scores(dealer_state)
        if player_scores(player_state) > 21:
            print(f"Your sum is {player} hence Dealer wins!")
            restart()
        elif player_scores(dealer_state) > 21:
            print(f"The Dealer's sum is {dealer} hence you win!")
            restart()
        elif player_scores(player_state) == 21 and player_scores(dealer_state) == 21:
            print("The game is a draw!")
            restart()
        elif player_scores(dealer_state) == 21:
            print("The Dealer's sum is 21 hence they win!")
            restart()
        elif player_scores(player_state) == 21:
            print("Your sum is 21 you win!")
            restart()
        elif player_scores(player_state) == player_scores(dealer_state):
            print(f"Draw! Player sum:{player} Dealer sum:{dealer}")
            restart()
        elif player_scores(player_state) > player_scores(dealer_state):
            print(f"The player wins! Player sum:{player} Dealer sum:{dealer}")
            restart()
        else:
            print(f"Dealer Wins! Player sum:{player} Dealer sum:{dealer}")
            restart()
