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

    def consume(self):
        print("Your resources decrease")


class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name)
        self.attack = attack

    def attack(self):
        print("You attacked the enemy with %s" % self.name)


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", 10)

    def stab(self):
        print("You stabbed the enemy")


class Gun(Weapon):
    def __init__(self, name, attack):
        super(Gun, self).__init__(name, attack)

    def use_ammo(self):
        print("You used a gun")

    def shoot(self):
        print("enemies health decreased")

    def reload(self):
        print("You reload")


class Handgun(Gun):
    def __init__(self):
        super(Handgun, self).__init__("Pistol", 30)


class Shotgun(Gun):
    def __init__(self):
        super(Shotgun, self).__init__("Shotgun", 50)


class Ammo(Consumable):
    def __init__(self, name, amount):
        super(Ammo, self).__init__(name, amount)
        self.amount = amount

    def use(self):
        print("your ammo is decreased")


class HgAmmo(Ammo):
    def __init__(self):
        super(HgAmmo, self).__init__("handgun ammo", 5)

    def add_ammo(self):
        print("You received more handgun ammo")


class SgShells(Ammo):
    def __init__(self):
        super(SgShells, self).__init__("shotgun shells", 6)

    def add_shells(self):
        print("You received more shells")


class Dagger(Consumable):
    def __init__(self):
        super(Dagger, self).__init__("dagger", 1)

    def kill(self):
        print("You instantly killed a zombie.")


class Grenade(Consumable):
    def __init__(self):
        super(Grenade, self).__init__("grenade", 1)

    def blow_up(self):
        print("You blew a zombie up")


class Herb(Consumable):
    def __init__(self, name, effect):
        super(Herb, self).__init__(name, effect)

    def heal(self):
        print("You heal")


class GrnHerb(Herb):
    def __init__(self):
        super(GrnHerb, self).__init__("green herb", 20)

    def half_heal(self):
        print("You heal halfway")


class RedHerb(Herb):
    def __init__(self):
        super(RedHerb, self).__init__("red herb", 50)

    def full_heal(self):
        print("You fully heal")
