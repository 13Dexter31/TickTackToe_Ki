from enum import Enum

class Feedback(Enum):
    PLACE_OCCUPIED = 1
    WRONG_INPUT = 2
    GAME_LOST = 3
    GAME_WON = 4
    GAME_DRAW = 5