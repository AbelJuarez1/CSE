class Room(object):
    def __init__(self, name, north, east, south, west, northeast, northwest, southeast, southwest,
                 items, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.ne = northeast
        self.nw = northwest
        self.se = southeast
        self.sw = southwest
        self.items = items
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
main_hall = Room("Main Hall", None, "sgal", None, "dining", "mirror1", None, None, None, None,
                 "The Main Hall seems to be very"
                 " empty. There is a typewriter in the corner to save your "
                 "progress. One door is to the west, east, and northeast.")

dining = Room("Dining Room", "tea", "main_hall", None, None, None, None, None, None, "blue crystal",
              "A big table is in the middle of the room with a blue crystal in the middle."
              " One door leads east, and another leads north")

tea = Room("Tea Room", "vulture", None, "dining", None, "piano", None, None, None, None,
           "You find one of your friends dead on the floor. A zombie walks toward you."
                       " There is a door to the south, north, and northeast.")

piano = Room("Piano Room", None, None, "tea", None, None, None, None, None, "ammo",
             "There is a piano with a music score on it. An ammo clip lays on top of a bar stool."
             " The only exit is to the south.")

vulture = Room("Vulture-Head Room", None, "tiger", "tea", "keeper", None, "ne", None, None, None,
               "Insert Description")

tiger = Room("Tiger Room", None, "plant", "vulture", None, None, None, None, None, "ammo",
             "A lone statue of a tiger's head stands on the wall. It has a plaque that reads,'Some tigers "
             "have a red and blue eye. A door leads south and east.")

plant = Room("Plant Room", None, None, None, "tiger", None, None, None, None, "herb" "herb",
             "There is a monstrous plant that seems to be in your way. Past it are some herbs. The only exit"
             "is to the west.")

keeper = Room("Keeper's Bedroom", None, "vulture", None, None, None, None, None, None, "diary" "key",
              "The room is small with a big bed right in the middle. A body is laying on the floor, "
              "and a diary with a key lay open on the desk. The only exit is to the east.")

nw = Room("North-West Corridor", None, None, "safe1", None, None, None, None, None, None, "Insert Description")

safe1 = Room("Safe Room", "nw", None, None, None, None, None, None, None, None,
             "There is a box in here to place your items and a typewriter to save your progress. The only"
             "exit leads north.")

mirror = Room("Mirror Room", None, None, None, "main_hall", None, None, "costume", None, None, "Insert Description")

sgal = Room("Small Gallery", None, "dog", None, "main_hall", None, None, None, None, None, "Insert Description")

costume = Room("Costume Room", "mirror", None, None, None, None, None, None, None, None, "Insert Description")

dog = Room("Hallway", "ne", None, None, "sgal", None, None, None, None, "ammo",
           "Your in a long hallway with a couple of ammo clips laying around. A couple of dogs are blocking"
           "the way north. You can go back west if you need.")

ne = Room("North-East Room", "bath", "boiler", "dog", "crow", None, None, None, None, "ceiling", "Insert Description")

bath = Room("Bathroom", None, None, "ne", None, None, None, None, None, None,
            "There is a bathtub filled with dirty water. It seems that thee is something shining inside of of"
            "it. One exit leads south.")

boiler = Room("Boiler Room", None, None, None, "ne", None, None, None, None, None, "Insert Description")

crow = Room("Gallery", "safe2", "ne", None, "outside", None, "Study", None, None, None, "Insert Description")

safe2 = Room("Safe Room", None, None, "crow", None, None, None, None, None, None,
             "There is a box for your items and a typewriter to save your progress. The only"
             "exit leads south.")

study = Room("Study", None, None, "crow", None, None, None, None, None, None, "Insert Description")

outside = Room("Outside Corridor", "shed", "crow", None, None, None, None, None, None, None, "Insert Description")

shed = Room("Shed", None, None, "outside", None, None, None, None, None, None, "Insert Description")

ceiling = Room("Ceiling Room", None, None, "shotgun", None, None, None, None, None, None, "Insert Description")

shotgun = Room("Shotgun Room", "ceiling", None, None, None, None, None, None, None, None, "Insert Description")
