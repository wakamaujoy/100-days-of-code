alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        encode = alphabet[new_position]
        cipher_text += encode
    print(f"The encoded text is {cipher_text}")
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, input):
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.

    decipher_text =""
    for letter2 in text:
        position2 = alphabet.index(letter2)
        new_position2 = position2 - shift
        decode = alphabet[new_position2]
        decipher_text += decode
    print(f"The decoded text is {decipher_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(text,shift)
elif direction =="decode":
    decrypt(text,shift)
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
#encrypt(text, shift)
#decrypt(text,shift)



