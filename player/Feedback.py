from enum import Enum

class Feedback(Enum):
    PLACE_OCCUPIED = 0
    WRONG_INPUT = 1
    GAME_LOST = 2
    GAME_WON = 3
    GAME_DRAW = 4