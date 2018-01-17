import random
# Abel Juarez
money = 15
rounds = 0
while money > 0:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    print("rolled: %s" % total)
    print("money: %s" % money)
    rounds += 1
    print(rounds)

    if d1 + d2 == 7:
        money += 4
        print(money)
    else:
        money -= 1
        print(money)


