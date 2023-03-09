#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]
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

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


display =[]
for _ in chosen_word:
    display += "_"
print(display)

for blank in display:
    guess = input("Guess a letter ").lower()
            #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

            #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
            #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    for position in range(len(chosen_word)):
     letter = chosen_word[position]
     if guess ==letter:
      display[position] = letter
    print(display)


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
   # print(f"{' '.join(display)}")
# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
