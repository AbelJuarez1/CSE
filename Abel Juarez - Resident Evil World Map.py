mansion_map = {
    'MAINHALL': {
        'NAME': "Main Hall",
        'DESCRIPTION': "The Main Hall seems to be very empty. There is a typewriter in the corner. "
                       "One door is to the west, east, and northeast.",
        'PATHS': {
            'WEST': 'DININGROOM',
            'EAST': 'SGALLERY',
            'NORTHEAST': 'MIRRORROOM1'
        }
    },
    'DININGROOM': {
        'NAME': "Dining Room",
        'DESCRIPTION': "",
        'PATHS': {
            'EAST': 'MAINHALL',
            'NORTH': 'TEAROOM'
        }
    },
    'TEAROOM': {
        'NAME': "Tea Room",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': 'DINING ROOM',
            'NORTH': 'VULTUREHEAD',
            'NORTHEAST': 'PIANOROOM'
        }
    },
    'PIANOROOM': {
        'NAME': "Piano Room",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': 'TEAROOM'
        }
    },
    'VULTUREHEAD': {
        'NAME': "Vulture Head Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': 'TEAROOM',
            'WEST': 'KEEPERSROOM',
            'NORTHWEST': 'NORTHWESTCORRIDOR',
            'EAST': 'TIGERRROOM'
        }
    },
    'TIGERROOM': {
        'NAME': "Tiger Room",
        'DESCRIPTION': "There are paintings of tigers everywhere. To the east seems to be a weak wall.",
        'PATHS': {
            'SOUTH': 'VULTUREHEAD',
            'EAST': 'PLANTROOM'
        }
    },
    'PLANTROOM': {
        'NAME': "Plant Room",
        'DESCRIPTION': "There is a monstrous plant that seems to be in your way.Past it are some herbs. ",
        'PATHS': {
            'WEST': 'TIGERROOM'
        }
    },
    'KEEPERSROOM': {
        'NAME': "Keeper's Bedroom",
        'DESCRIPTION': "",
        'PATHS': {
            'EAST': 'VULTUREHEAD'
        }
    },
    'NORTHWESTCORRIDOR': {
        'NAME': "North-West Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': 'SAFEROOM'
        }
    },
    'SAFEROOM1': {
        'NAME': "Safe Room",
        'DESCRIPTION': "There is a box in here to place your items.",
        'PATHS': {
            'NORTH': 'NORTHWESTCORRIDOR'
        }
    },
    'MIRROR': {
        'NAME': "Mirror Room",
        'DESCRIPTION': "",
        'PATHS': {
            'WEST': 'MAINHALL',
            'SOUTHEAST': 'COSTUME'
        }
    },
    'SGALLERY': {
        'NAME': "Small Gallery",
        'DESCRIPTION': "",
        'PATHS': {
            'EAST': 'DOG',
            'WEST': 'MAINHALL'
        }
    },
    'COSTUME': {
        'NAME': "Costume Room",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': 'MIRROR'
        }
    },
    'DOG': {
        'NAME': "HALLWAY",
        'DESCRIPTION': "",
        'PATHS': {
            'WEST': 'SGALLERY',
            'NORTH': 'NEROOM'
        }
    },
    'NEROOM': {
        'NAME': "Northeast Room",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': 'BATH',
            'EAST': 'BOILER',
            'WEST': 'CROW',
            'SOUTH': 'DOG',
            'SOUTHWEST': 'CEILING'
        }
    },
    'BATH': {
        'NAME': "Bathroom",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': 'NEROOM'
        }
    },
    'BOILER': {
        'NAME': "Boiler Room",
        'DESCRIPTION': "",
        'PATHS': {
            'WEST': 'NEROOM'
        }
    },
}

current_node = mansion_map['MAINHALL']
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'NORTHEAST', 'NORTHWEST', 'SOUTHEAST', 'SOUTHWEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = mansion_map[name_of_node]
        except KeyError:
            print("You can't go that way.")
    else:
        print('Command not recognized')
        print()
