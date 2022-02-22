from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text,shift,direction):
    if direction=='decode':
        shift*=-1
    answer=""
    for letter in text:
        answer+=alphabet[(alphabet.index(letter)+shift)%26]
    print(f"The {direction}d word is {answer}")

start_flag=True

while start_flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(text,shift,direction)

    quit_flag=input("Would you like to continue? Type 'yes' to continue:\n")

    if quit_flag!='yes':
        start_flag=False
    



