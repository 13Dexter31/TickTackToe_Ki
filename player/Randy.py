from random import randint

from player.Player import Player


class Randy(Player):

    def makeMove(self, board):
        return Position(randint(1, 3), randint(1, 3))

    def giveFeedback(self):
        pass