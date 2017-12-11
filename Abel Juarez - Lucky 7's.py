import random
# Abel Juarez

money = 15
d1 = (random.randint(1, 6))
d2 = (random.randint(1, 6))

print(d1 + d2)

turn = input("Press Enter to Roll Again")

if str(money) <= str(0):
    quit()
