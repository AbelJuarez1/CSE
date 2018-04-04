class Character(object):
    def __init__(self, name, inventory, health, stats, attack):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.stats = stats
        self.attack_amt = attack

    def attack(self, target):
        target.damage(self.attack_amt)

    def take_damage(self, dmg):
        self.health(dmg)

    # def interact(self, item):
    #     item.inventory


player = Character("You", None, 100, None, 25)
enemy = Character("enemy", None, 50, None, 20)

