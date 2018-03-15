class Item(object):
    def __init__(self, name, weapon, consumable):
        self.name = name
        self.weapon = weapon
        self.consumable = consumable

    def use_item(self):
        print("You used %s" % self.consumable)


class Weapon(Item):
    def __init__(self, name, weapon, attack):
        super(Weapon, self).__init__(name, weapon, attack)
        self.attack = attack

    def attack(self):
