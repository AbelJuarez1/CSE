world_map = {
    'WESTHOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You are west of a white house.",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'DESCRIPTION': "You are north of a white house.",
        'NAME': "North of House",
        'PATHS': {
            'SOUTH': 'WESTHOUSE',
        }
    },
    'SOUTHHOUSE': {
        'NAME': "South of house",
        'DESCRIPTION': "You are south of a white house.",
        'PATHS': {
            'NORTH': 'WESTHOUSE'
        }
    }
}
