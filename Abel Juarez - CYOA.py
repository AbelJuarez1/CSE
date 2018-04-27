# import random
# - import statements
# - class definition
#       1. items
#       2. characters
#       3. rooms
# - controller


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


class ZombieClaws(Weapon):
    def __init__(self):
        super(ZombieClaws, self).__init__("Zombie Claws", 50)


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
        super(Handgun, self).__init__("pistol", 10)


class Shotgun(Gun):
    def __init__(self):
        super(Shotgun, self).__init__("shotgun", 20)


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
        super(SgShells, self).__init__("shotgun shells", 4)

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


class Character(object):
    def __init__(self, name, health, stats, weapon):
        self.name = name
        self.inventory = []
        self.health = health
        self.stats = stats
        self.weapon = weapon

    def attack(self, target):
        target.damage(self.weapon.damage)

    def take_damage(self, dmg):
        self.health(dmg)

    def inventory(self):
        self.inventory(Item)
    # def interact(self, item):
    #     item.inventory


knife = Knife()
shot = Shotgun()
gherb = GrnHerb()
rherb = RedHerb()
pistol = Handgun()
grenade = Grenade()
dagger = Dagger()
shotgunammo = Ammo("shotgun shells", 4)
pistolammo = Ammo("handgun ammo", 5)
zombie = ZombieClaws()

player = Character("You", None, 100, None, knife)
enemy = Character("zombie", None, 50, None, shot)
crimson = Character("crimson", None, 200, None, ZombieClaws)
plant_enemy = Character("large plant", None, 300, None, None)
cerberus = Character("Cerberus", None, 75, None, None)
crow = Character("Crow", None, None, None, None)


class Room(object):
    def __init__(self, name, north, east, south, west, northeast, northwest, southeast, southwest,
                 items, character, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        self.items = items
        self.character = character
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
main_hall = Room("Main Hall", None, "sgal", None, "dining", "mirror", None, None, None, [pistol], None,
                 "The Main Hall seems to be very"
                 " empty. There is a typewriter in the corner to save your "
                 "progress. One door is to the west, east, and northeast.")

dining = Room("Dining Room", "tea", "main_hall", None, None, None, None, None, None, [shotgunammo], None,
              "A big table is in the middle of the room with a blue crystal in the middle."
              " One door leads east, and another leads north")

tea = Room("Tea Room", "vulture", None, "dining", None, "piano", None, None, None, None, [enemy],
           "You find one of your friends dead on the floor. A zombie walks toward you."
                       " There is a door to the south, north, and northeast.")

piano = Room("Piano Room", None, None, "tea", None, None, None, None, None, [pistolammo], [enemy, crimson],
             "There is a piano with a music score on it. An ammo clip lays on top of a bar stool."
             " The only exit is to the south.")

vulture = Room("Vulture-Head Room", None, "tiger", "tea", "keeper", None, "ne", None, None, [gherb], [enemy, enemy,
                                                                                                      crimson],
               "Insert Description")

tiger = Room("Tiger Room", None, "plant", "vulture", None, None, None, None, None, [shotgunammo], None,
             "A lone statue of a tiger's head stands on the wall. It has a plaque that reads,'Some tigers "
             "have a red and blue eye. A door leads south and east.")

plant = Room("Plant Room", None, None, None, "tiger", None, None, None, None, [gherb, rherb], [plant_enemy],
             "There is a monstrous plant that seems to be in your way. Past it are some herbs. The only exit"
             "is to the west.")

keeper = Room("Keeper's Bedroom", None, "vulture", None, None, None, None, None, None, [dagger], [enemy, enemy],
              "The room is small with a big bed right in the middle. A body is laying on the floor, "
              "and a diary with a key lay open on the desk. The only exit is to the east.")

nw = Room("North-West Corridor", None, None, "safe1", None, None, None, None, None, None, [enemy, crimson],
          "Insert Description")

safe1 = Room("Safe Room", "nw", None, None, None, None, None, None, None, None, None,
             "There is a box in here to place your items and a typewriter to save your progress. The only"
             "exit leads north.")

mirror = Room("Mirror Room", None, None, None, "main_hall", None, None, "costume", None, [gherb, gherb, grenade],
              None,
              "Insert Description")

sgal = Room("Small Gallery", None, "dog", None, "main_hall", None, None, None, None, None, [enemy],
            "Insert Description")

costume = Room("Costume Room", "mirror", None, None, None, None, None, None, None, None, None,
               "Insert Description")

dog = Room("Hallway", "ne", None, None, "sgal", None, None, None, None, [pistolammo], [cerberus, cerberus],
           "Your in a long hallway with a couple of ammo clips laying around. A couple of dogs are blocking"
           "the way north. You can go back west if you need.")

ne = Room("North-East Room", "bath", "boiler", "dog", "crow", None, None, None, "ceiling", None, None,
          "Insert Description")

bath = Room("Bathroom", None, None, "ne", None, None, None, None, None, None, [enemy],
            "There is a bathtub filled with dirty water. It seems that thee is something shining inside of of"
            "it. One exit leads south.")

boiler = Room("Boiler Room", None, None, None, "ne", None, None, None, None, [rherb], [cerberus, cerberus],
              "Insert Description")

crow = Room("Gallery", "safe2", "ne", None, "outside", None, "Study", None, None, None, [crow],
            "There isn't much here but a couple of annoying crows. There are paths to the north, east, "
            "west, and northwest.")

safe2 = Room("Safe Room", None, None, "crow", None, None, None, None, None, [shotgunammo, gherb, gherb, dagger,
                                                                             pistolammo], None,
             "There is a box for your items and a typewriter to save your progress. The only"
             "exit leads south.")

study = Room("Study", None, None, "crow", None, None, None, None, None, None, [crimson, crimson, crimson],
             "Insert Description")

outside = Room("Outside Corridor", "shed", "crow", None, None, None, None, None, None, None, [crimson, cerberus],
               "Insert Description")

shed = Room("Shed", None, None, "outside", None, None, None, None, None, [gherb, gherb, dagger, grenade], None,
            "Insert Description")

ceiling = Room("Ceiling Room", None, "ne", "shotgun", None, None, None, None, None, [pistolammo], None,
               "Insert Description")

shotgun = Room("Shotgun Room", "ceiling", None, None, None, None, None, None, None, [Shotgun], None,
               "There is a shotgun on the wall. The only exit is to the north.")

current_node = main_hall
directions = ['north', 'east', 'south', 'west', 'northwest', 'northeast', 'southwest', 'southeast']
short_directions = ['n', 'e', 's', 'w', 'nw', 'ne', 'sw', 'se']
inventory = []


while True:
    print(current_node.name)
    print(current_node.description)
    if current_node.items is None:
        print("There are no items in the room")
    else:
        print("There are the following items in the room:")
        for i, n in enumerate(current_node.items):
            print("%d : %s" % (i+1, n.name))
    if current_node.character is None:
        print("There are no enemies in the room")
    else:
        print("There are these enemies in the room:")
        for i, n in enumerate(current_node.character):
            print("%d : %s" % (i+1, n.name))

    command = input('>_').lower()
    print()
    if 'quit' in command:
        quit(0)
    elif command in short_directions:
        # look for which command we typed in
        pos = short_directions.index(command)
        # change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can't go that way.")
            print()
    else:
        print('Command not recognized')
        print()

    if 'take' in command:
        item_requested = command[5:]
        found = False
        for item in current_node.items:
            if item.name == item_requested:
                player.inventory.append(item)
                for item in player.inventory:
                    print("You take the %s" % item_requested)
                    print("You have a %s in your inventory" % item.name)
                found = True
                current_node.items.remove(item)
        if not found:
            print("This item isn't here buddy.")
            print()
    if 'attack' in command:
        attack = command[5:]
