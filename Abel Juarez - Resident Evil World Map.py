mansion_map = {
    'MAINHALL': {
        'NAME': "Main Hall",
        'DESCRIPTION': "",
        'PATHS': {
            'WEST': 'DININGROOM',
            'EAST': 'SMALLGALLERY',
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
    }
}
