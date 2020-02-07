"""

Hangman Lab
Tashi Bapu - 2020

Welcome to Tashi's Hangman Game.

    Rules:
            - Guess with only 1 letter at a time.
            - You have seven drawings of the hangman before you lose.
            - GLHF!

    Goal:
            - Guess the hidden word.
"""

import random

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
]  # Hangman Pictures

def purple(skk): print("\033[95m {}\033[00m" .format(skk))  # Purple Colored Text

def game_again():
    print("_________________________________________________________________________________")
    answer = input("\nWould You Like To Play Again? (Yes or No): ".lower())
    if answer == "yes":
        game()

def the_word():
    word_list = ["LAME", "MINECRAFT", "MONKEY", "MONEY", "SOFT", "HARD", "WEAK", "EASY", "BEHIND"]
    return random.choice(word_list)

def game():
    abcs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Alphabet List/Check
    word = the_word()
    used_letters = []
    whats_left = ""  # For Printing Later Guessed And Missing Letters (Later On)
    pic = 0  # For Gallows Index
    done = False

    # Introduction Format
    print('''
    Welcome to Tashi's Hangman Game.
    
    Rules:
            - Guess with only 1 letter at a time.
            - You have seven drawings of the hangman before you lose.
            - GLHF!
                                Game Start!                       
_________________________________________________________________________________''')
    print(gallows[pic])
    print(" Used Letters: ", used_letters)
    print("", len(word) * " _ ")

    while done is False:  # Main Game Loop

        if done is False:
            guess = input(" Guess A Letter: ").upper()

        print('''
_________________________________________________________________________________''')

        print("\n", gallows[pic])

        if len(guess) == 1:  # Checking If Guess Is Only 1 Character

            # Incorrect Enters
            if guess not in abcs:  # Checking if Guess Is A Letter
                purple("You Have Not Entered A Letter.")

            elif guess in used_letters:  # Checking If Guess Is A Repeated Letter
                purple("You Have Already Entered That Letter.")

            # Correct Enters
            elif guess in word:  # Checking If Guess Is A Letter In Word
                purple("Good Job, That Letter Is In The Word!")
                used_letters.append(guess)

            elif guess in abcs and guess not in word:  # Checking If Guess Is Wrong
                purple("Nice Try, But That Letter Is Not In The Word.")
                used_letters.append(guess)
                pic += 1  # Changing Hangman Picture

        else:
            purple("You May Only Enter One Character At A Time.")

        print(" Used Letters: ", used_letters)

        for letter in word:  # Prints (Missing) Letter In Correct Order
            if letter in used_letters:
                whats_left += letter
            else:
                whats_left += " _ "

        print(whats_left)

        if whats_left == word:  # Checking If The Word Has Been Guessed
            purple("Amazing Job, You Have Guessed The Correct Word!")
            done = True

        elif gallows[pic] == gallows[6]:  # Checking Last Try To Guess
            print(gallows[pic])
            purple("The Hangman Is Completed! You Lose!")
            done = True

        whats_left = ""  # Resets The Printed (Missing) Letters (IMPORTANT!)

game()  # Starts Game
game_again()  # Asking User If They Want To Play Again