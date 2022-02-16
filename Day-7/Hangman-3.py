import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')


word_len=len(chosen_word)
display=['_']*word_len

#TODO-1: - Use a while loop to let the user guess again. 
#The loop should only stop once the user has guessed all the 
#letters in the chosen_word and 'display' has no more blanks ("_"). 
#Then you can tell the user they've won.
game_state=True
while game_state:
    guess = input("Guess a letter: ").lower()

    for i in range(word_len):
        if chosen_word[i] == guess:
            display[i]=guess

    print(display)

    if not '_' in display:
        game_state=False
print("you've won")