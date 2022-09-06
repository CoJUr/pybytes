#
#
#F-string and simple if/else:
# MIN_DRIVING_AGE = 18
#
#
# def allowed_driving(name, age):
#     """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
#        checking the passed in age against the MIN_DRIVING_AGE constant"""
#     is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
#     print(f'{name} {is_allowed} to drive')


# def print_colors():
#     """In the while loop ask the user to enter a color,
#        lowercase it and store it in a variable. Next check:
#        - if 'quit' was entered for color, print 'bye' and break.
#        - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
#        - otherwise print the color in lower case."""
#     while True:
#         color = input('Enter a color: ').lower()
#         if color == 'quit':
#             print('bye')
#             break
#
#         if color not in VALID_COLORS:
#             print('Not a valid color')
#             continue
#
#         print(color)

GAME_STATS = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


# def print_game_stats(games_won):
#     """Loop through games_won's dict (key, value) pairs (dict.items)
#        printing (print, not return) how many games each person has won,
#        pluralize 'game' based on number.
#
#        Expected output (ignore the docstring's indentation):
#
#        sara has won 0 games
#        bob has won 1 game
#        tim has won 5 games
#        julian has won 3 games
#        jim has won 1 game
#
#        (Note that as of Python 3.7 - which we're using atm - dict insert order
#        is retained so no sorting is required for this Bite.)
#     """
#     for name, num_games in games_won.items():
#         games = "game" if num_games == 1 else "games"
#         print(f'{name} has won {num_games} {games}')