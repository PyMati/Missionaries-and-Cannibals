"""Module with all configuration data."""

WINDOW_SIZE = (800, 600)

MAX_FPS = 120

COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0)
}

GAME_FONT = ('freesansbold.ttf', 48)
INSTRUCTIONS_FONT = ('freesansbold.ttf', 12)

MOVE_SPEED = 2.5

GAMEGRAPH = {"win": ["-", "g", "g", "g", "c", "c", "c"],
             "lose": [
                 ["c", "g", "g", "-", "g", "c", "c"],
                 ["c", "c", "g", "-", "g", "g", "c"],

                 ["c", "c", "g", "g", "g", "-", "c"],
                 ["c", "c", "-", "g", "g", "g", "c"],
                 
                 ["c", "-", "g", "g", "g", "c", "c"],
                 ["c", "g", "g", "g", "-", "c", "c"],
             ]
             }
