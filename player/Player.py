from abc import abstractmethod

from player.Feedback import Feedback

class Player():

    def makeMove(self, board):

        position = self.getPosition(board)

        if(not board.isEmpty(position)):
            self.giveFeedback(Feedback.PLACE_OCCUPIED)
            position = self.makeMove(board)

        return position

    @abstractmethod
    def getPosition(self, board):
        pass

    @abstractmethod
    def giveFeedback(self):
        pass


