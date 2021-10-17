from abc import abstractmethod

from player.Feedback import Feedback

class Player():

    def __init__(self, representationChar) -> None:
        self.representationChar = representationChar

    def __str__(self):
        return self.representationChar

    @abstractmethod
    def makeMove(self, board):
        pass

    @abstractmethod
    def giveFeedback(self):
        pass


