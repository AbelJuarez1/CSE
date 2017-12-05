import random  # Abel Juarez

# step one) generate random number
# step two) take an input (number) from the user
# step three) compare input to generated number
# step four) add "higher" and "lower" statements
# step five) add 5 guesses

print("Try to guess the number I'm thinking of.")
print("You have 5 guess or it's game over.")
print("Get it right and it's...still...game over...")

random_number = 'random.randint'
print(random.randint(1, 50))
number = input()


def equal_number():
    if random_number == number:
        return "good job"
