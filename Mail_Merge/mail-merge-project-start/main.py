#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited:
    invitees = invited.readlines()
    # print(invitees)

with open("./Input/Letters/invites.txt", mode="r") as letter:
    letter_contents = letter.read()
    # print(letter_contents)

for name in invitees:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    with open(f"Letter_for_{stripped_name}", mode="w") as individual_letter:
        each_letter = individual_letter.write(new_letter)





