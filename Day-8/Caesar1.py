alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    answer=""
    for letter in text:
        answer+=alphabet[(alphabet.index(letter)+shift)%26]
    print(f"The encoded word is {answer}")

def decrypt(text,shift):
    answer=""
    for letter in text:
        answer+=alphabet[(alphabet.index(letter)-shift)%26]
    print(f"The decoded word is {answer}")

if direction=='encode':
    encrypt(text,shift)
elif direction=='decode':
    decrypt(text,shift)