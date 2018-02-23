mansion_map = {
    'MAINHALL': {
        'NAME': "Main Hall",
        'DESCRIPTION': "The Main Hall seems to be very empty. There is a typewriter in the corner to save your "
                       "progress. One door is to the west, east, and northeast.",
        'PATHS': {
            'WEST': 'DININGROOM',
            'EAST': 'SGALLERY',
            'NORTHEAST': 'MIRRORROOM1'
        }
    },
    'DININGROOM': {
        'NAME': "Dining Room",
        'DESCRIPTION': "A big table is in the middle of the room with a blue crystal in the middle."
                       " One door leads east, and another leads north",
        'PATHS': {
            'EAST': 'MAINHALL',
            'NORTH': 'TEAROOM'
        }
    },
    'TEAROOM': {
        'NAME': "Tea Room",
        'DESCRIPTION': "You find one of your friends dead on the floor. A zombie walks toward you."
                       " There is a door to the south, north, and northeast.",
        'PATHS': {
            'SOUTH': 'DININGROOM',
            'NORTH': 'VULTUREHEAD',
            'NORTHEAST': 'PIANOROOM'
        }
    },
    'PIANOROOM': {
        'NAME': "Piano Room",
        'DESCRIPTION': "There is a piano with a music score on it. An ammo clip lays on top of a bar stool."
                       " The only exit is to the south.",
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
        'DESCRIPTION': "A lone statue of a tiger's head stands on the wall. It has a plaque that reads,'Some tigers "
                       "have a red and blue eye. A door leads south and east.",
        'PATHS': {
            'SOUTH': 'VULTUREHEAD',
            'EAST': 'PLANTROOM'
        }
    },
    'PLANTROOM': {
        'NAME': "Plant Room",
        'DESCRIPTION': "There is a monstrous plant that seems to be in your way. Past it are some herbs. The only exit"
                       "is to the west.",
        'PATHS': {
            'WEST': 'TIGERROOM'
        }
    },
    'KEEPERSROOM': {
        'NAME': "Keeper's Bedroom",
        'DESCRIPTION': "The room is small with a big bed right in the middle. A body is laying on the floor, "
                       "and a diary with a key lay open on the desk. The onlt eit is to the east.",
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
        'DESCRIPTION': "There is a box in here to place your items and a typewriter to save your progress. The only"
                       "exit leads north.",
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
        'DESCRIPTION': "Your in a long hallway with a couple of ammo clips laying around. Acouple of dogs are blocking"
                       "the way north. You can go back west if you need.",
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
        'DESCRIPTION': "There is abathtub filled with dirty water. It seems that thee is something shining inside of of"
                       "it. ONe exit leads south.",
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
    'CROW': {
        'NAME': "Gallery",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': 'SAFEROOM2',
            'EAST': 'NEROOM',
            'WEST': 'OUTSIDE',
            'NORTHWEST': 'STUDY'
        }
    },
    'SAFEROOM2': {
        'NAME': "Safe Room",
        'DESCRIPTION': "There is a box for your items and a typewriter to save your progress. The only"
                       "exit leads south.",
        'PATHS': {
            'SOUTH': 'CROW'
        }
    },
    'STUDY': {
        'NAME': "Study",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': 'CROW'
        }
    },
    'OUTSIDE': {
        'NAME': "Outside Corridor",
        'DESCRIPTION': "",
        'PATHS': {
            'EAST': 'CROW',
            'NORTH': 'SHED'
        }
    },
    'SHED': {
        'NAME': "Shed",
        'DESCRIPTION': "",
        'PATHS': {
            'SOUTH': 'OUTSIDE'
        }
    },
    'CEILING': {
        'NAME': "Ceiling Room",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTHEAST': 'NEROOM',
            'SOUTH': 'SHOTGUN'
        }
    },
    'SHOTGUN': {
        'NAME': "Shotgun Room",
        'DESCRIPTION': "",
        'PATHS': {
            'NORTH': 'CEILING'
        }
    },
}

current_node = mansion_map['MAINHALL']
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'NORTHEAST', 'NORTHWEST', 'SOUTHEAST', 'SOUTHWEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    print()
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = mansion_map[name_of_node]
        except KeyError:
            print("You can't go that way.")
            print()
    else:
        print('Command not recognized')
        print()
