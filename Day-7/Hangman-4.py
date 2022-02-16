import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_len=len(chosen_word)
display=['_']*word_len

gamer_lives=6
game_state=True
while game_state:
    guess = input("Guess a letter: ").lower()
    if not guess in chosen_word:
        print("wrong guess")
        gamer_lives-=1 
    else:
        for i in range(word_len):
            if chosen_word[i] == guess:
                display[i]=guess
                print("correct guess")
        
    print(display)
    print(stages[gamer_lives])

    if not '_' in display:
        game_state=False
    elif gamer_lives==0:
        game_state=False
if gamer_lives>0:
    print("you've won")
else:
    print("you lost")