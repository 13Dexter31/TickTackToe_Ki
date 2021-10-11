from random import randint

from player.Player import Player


class Randy(Player):

    def getPosition(self):
        return Position(randint(1, 3), self.getRandomRow())

    def getRandomRow(self):
        random = randint(1, 3)
        if(random == 1):
            return 'A'
        elif(random == 2):
            return 'B'
        elif(random == 3):
            return 'C'

    def giveFeedback(self):
        pass