alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
    end_text=""
    for letter in text:
        position = alphabet.index(letter)
        if direction =="encode":
            new_position = position + shift
            new_letter = alphabet[new_position]
            end_text += new_letter
        elif direction == "decode":
            new_position =position - shift
            new_letter = alphabet[new_position]
            end_text +=new_letter

    print(f"Your {direction}d message is {end_text}")

caesar(text,shift,direction)