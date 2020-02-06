'''

Hangman Lab
Tashi Bapu - 2020

'''

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again

import random

# Variables/Lists
gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]
letters_used = []
letters_wrong = 0
word_list = ["CHILD", "JAMES", "TASHI"]
word = word_list.pop(random.randrange(len(word_list)))
playing = True

space1 = "_"
space2 = "_"
space3 = "_"
space4 = "_"
space5 = "_"


# Def

def game():

    global space1, space2, space3, space4, space5, letters_wrong, letters_used

    print(gallows[letters_wrong])

    if len(word) == 5:
        print(
        "   ", space1, space2, space3, space4, space5
        )

    print('''
    Letters You Used: ''', letters_used)

    guess = input(str('''
    Enter A Letter: '''))

    if word == "CHILD":
        for letter in word:
            if guess.upper() == letter:
                if guess.upper() == "C":
                    space1 = "C"
                elif guess.upper() == "H":
                    space2 = "H"
                elif guess.upper() == "I":
                    space3 = "I"
                elif guess.upper() == "L":
                    space4 = "L"
                elif guess.upper() == "D":
                    space5 = "D"
                else:
                    letters_wrong += 1


    elif word == "JAMES":
        for letter in word:
            if guess.upper() == letter:
                if guess.upper() == "J":
                    space1 = "J"
                elif guess.upper() == "A":
                    space2 = "A"
                elif guess.upper() == "M":
                    space3 = "M"
                elif guess.upper() == "E":
                    space4 = "E"
                elif guess.upper() == "S":
                    space5 = "S"
                else:
                    letters_wrong += 1

    elif word == "TASHI":
        for letter in word:
            if guess.upper() == letter:
                if guess.upper() == "T":
                    space1 = "T"
                elif guess.upper() == "A":
                    space2 = "A"
                elif guess.upper() == "S":
                    space3 = "S"
                elif guess.upper() == "H":
                    space4 = "H"
                elif guess.upper() == "I":
                    space5 = "I"
                else:
                    letters_wrong += 1
    if letters_used.count(guess.upper()) == 0 and len(guess) == 1 and chr(65) <= guess >= chr(65 + 26):
        letters_used.append(guess.upper())
    elif letters_used.count(guess.upper()) is not 0:
        print('''
    You have already used that letter. Still Wrong. Guess Again.''')
    elif len(guess) is not 1:
        print('''
    Please Enter ONE letter at a time. Still Wrong. Guess Again.''')
    elif chr(65) > guess.upper() < chr(65 + 26):
        print('''
    Please Enter a LETTER. Still Wrong. Guess Again.''')



print('''
    Welcome to HangMan!
    Guess the 5 letter word to win! 
    But Make Sure Not To Complete
    The HangMan.
    If that happens... YOU LOSE!
    Good Luck!
''')

while playing is True:
    game()
