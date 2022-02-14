import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS=[rock,paper,scissors]

comp=random.randint(0,2)

user_input=int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissor\n"))

if (comp==2 and user_input==0) or (comp==1 and user_input==2) or (comp==0 and user_input==1):
    print(f"You Win! \n You Chose: {RPS[user_input]} \n Computer Chose:{RPS[comp]}")
elif (comp==user_input):
    print(f"It's a Tie! \n You Chose: {RPS[user_input]} \n Computer Chose:{RPS[comp]}")
elif (user_input>2 or user_input<0):
    print("Bruh! Wrong choice.")
else:
    print(f"You Lose! \n You Chose: {RPS[user_input]} \n Computer Chose:{RPS[comp]}")