import random
import string
# Abel Juarez
"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick an item from the list
3. Hide the word (use *)
4. Reveal letters already guessed
5. Create the win condition
"""

# print(string.ascii_lowercase)
word_bank = ["Spongebob Squarepants", "Patrick Star", "Sheldon Plankton", "Eugiene Krabs", "Gary the Snail",
             "Computer wife Karen", "Doodlebob", "Squidward Tentacles", "Sandy Cheeks", "Mermaid Man and Barnacle Boy"]
# random.shuffle()
# print(word_bank)
for item in word_bank:
    print(item)
