#Step 1"
import random
word_list= [ "boat" , "noise" , "number" ,"trail" ,"use" ,"fang" ,"tramp" ,"lettuce","mother","quill","scissors","desk","island"]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages= ['''
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
lives = 6
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


display =[]
for item in chosen_word:
    display += "_"
print(display)

end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter ").lower()
     #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
                #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess ==letter:
            display[position] = letter
            if guess  in display:
                print(f"You already guessed {guess}")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Won")


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -=1
        print(f"{guess} is not in the chosen word, try again")
        if lives ==0:
         end_of_game = True
         print("You Lose")
    #Join all the elements in the list and turn it into a String.
   # print(f"{' '.join(display)}")
# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
