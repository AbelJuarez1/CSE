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
word_bank = ["Spongebob Squarepants", "Patrick Star", "Sheldon Plankton", "Eugiene Krabs", "Gary the Snail",
             "Computer wife Karen", "Doodlebob", "Squidward Tentacles", "Sandy Cheeks", "Mermaid Man and Barnacle Boy"]
print(random.choice(word_bank))

while guesses > 0:


if 