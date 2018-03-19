class Item(object):
    def __init__(self, name):
        self.name = name

    def use_item(self):
        print("You used the %s" % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)


class Consumable(Item):
    def __init__(self, name, effect):
        super(Consumable, self).__init__(name)
        self.effect = effect


class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name, attack)
        self.attack = attack

    def attack(self):
        print("You attacked the enemy with %s" % self.name)


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", 10)


class Gun(Weapon):
    def __init__(self, name, attack):
        super(Gun, self).__init__(name, attack)


class Handgun(Gun):
    def __init__(self):
        super(Handgun, self).__init__("Pistol", 30)
