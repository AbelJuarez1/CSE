import random
import string
# Abel Juarez
"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick an item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""
guesses = 11
guess = " "
word_bank = ["SpongebobSquarepants", "PatrickStar", "SheldonPlankton", "EugeneKrabs", "GarytheSnail",
             "ComputerwifeKaren", "Doodlebob", "SquidwardTentacles", "SandyCheeks", "BarnacleBoy"]
letters_guessed = []
word = random.choice(word_bank)
correct_letter = list(word)

while guesses >= 2 != quit:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(" ".join(list(output)))
    if guess not in word:
        guesses -= 1
        print("guesses left: %s" % guesses)
    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    print(" ".join(letters_guessed))

# if output == word:
#     print("You win!")
#     exit(0)
