alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cypher(text, shift, direction):
    encrypted_text = ""
    if direction == "decode":
        shift *= -1
    for x in text:
        if x not in alphabet:
            encrypted_text += x
        else:
            let_pos = alphabet.index(x)
            encrypted_text += alphabet[shift + let_pos]
    print(encrypted_text)


from art import logo
should_end = False
print(logo)

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar_cypher(text, shift, direction)
    
    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") == "no":
        should_end = True
        print("Goodbye!")

