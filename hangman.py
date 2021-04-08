import random
from words import words 
import string 

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # set of letter in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what users has guessed 

    lives = 6

    #getting user input 
    # while loop will continue unless they guessed the word, or they don't have anymore lives
    while len(word_letters) > 0 and lives > 0 :
        #letters used 
        print("You have", lives, "lives left and you have used the letters: ", " ".join(used_letters))
        # words currently guessed 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: "," ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 
                print ("Letter is not in the word!")
        elif user_letter in used_letters:
            print("You've already used that character. Please use a different one!")
        else:
            print("Invalid character!")
    if lives == 0:
        print(f'You died! The word was {word} you donut.')
    else:
        print(f"You won! You guessed the word {word} correctly.")

hangman()