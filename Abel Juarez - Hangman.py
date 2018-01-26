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
guesses = 10
guess = " "
word_bank = ["Spongebob_Squarepants", "Patrick_Star", "Sheldon_Plankton", "Eugiene_Krabs", "Gary_the_Snail",
             "Computer_wife_Karen", "Doodlebob", "Squidward_Tentacles", "Sandy_Cheeks", "Mermaid_Man_and_Barnacle_Boy"]
letters_guessed = []
word = random.choice(word_bank)
correct_letter = list(word)

while guesses > 0 != quit:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)

    guess = input("Guess a letter: ")
    print("guesses left: %s" % guesses)
    letters_guessed.append(guess)
    print(" ".join(letters_guessed))