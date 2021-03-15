import random
from os import system, name 
from time import sleep 

# This creates a clear method to clear the terminal while running so things stay orderly :)
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

print()
print("--------------------------------------------------------------------")
print("Welcome to Python Byte - A Python version of the classic Hangman.")
print("Brought to you by your homie Jon Dawson!")
print("--------------------------------------------------------------------")
sleep(5)


while True:
    
    word = ""
    while len(word) < 5:
        word = random.choice(open('dictionary.txt').readlines())
    word = word.rstrip().lower()
    strikes = 0
    guesses = []
    wrong_guesses = []


    while strikes < len(word):
        
        clear()
        idk_var = ""
        print()
        for letter in word:
            if letter in guesses:
                print(letter, end="")
                idk_var += letter
            else:
                print("-", end="")
                idk_var += "-"
        
        print()
        print()
        print(f"Strike {strikes} out of {len(word)}")
        print()
        print(f"Previously guessed: {wrong_guesses}")
        print()
        
        
        while True:
            
            guess = input("Guess here: ").rstrip().lower()

            if guess in wrong_guesses:
                sleep(1)
                print()
                print("You've already guessed that!")
                sleep(2)
                break

            if guess in word:
                guesses += guess
                wrong_guesses += guess
                break
            else:
                strikes += 1
                wrong_guesses += guess
                break

        if strikes == len(word):
            print()
            print(f"You lost! The word was {word}!")
            print()
            sleep(2)
            print("Restarting...")
            sleep(2)
            break

        if idk_var == word:
            print()
            print("You win!")
            print()
            sleep(2)
            print("Restarting...")
            sleep(2)
            break
