class Room(object):
    def __init__(self, name, north, east, south, west, northeast, northwest, southeast, southwest, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.ne = northeast
        self.nw = northwest
        self.se = southeast
        self.sw = southwest
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
main_hall = Room("Main Hall", None, "sgal", None, "dining", "mirror1", None, None, None,
                 "The Main Hall seems to be very"
                 " empty. There is a typewriter in the corner to save your "
                 "progress. One door is to the west, east, and northeast.")

sgal = Room("")
