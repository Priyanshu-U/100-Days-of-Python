import random
import ascii_art as art
import word_list as wl
chosen_word = random.choice(wl.word_list)

print(art.logo)
print("\n")


word_len=len(chosen_word)
display=['_']*word_len

gamer_lives=6
game_state=True

while game_state:
    print(f"{display}\n")
    guess = input("Guess a letter: ").lower()
    
    if not guess in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        gamer_lives-=1 
    else:
        if guess in display:
            print(f"You've already guessed {guess}")
            continue
        else:
            for i in range(word_len):
                if chosen_word[i] == guess:
                    display[i]=guess
                    print("Correct Guess\n")
                

    print(art.stages[gamer_lives])

    if not '_' in display:
        game_state=False
    elif gamer_lives==0:
        game_state=False
if gamer_lives>0:
    print("You Win")
else:
    print("You Loose")