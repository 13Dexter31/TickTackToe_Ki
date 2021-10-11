from player.Feedback import Feedback
from player.Player import Player

class Human(Player):

    def getPosition(self, board):

        board.visualize()
        return Position(self.getColumn(), self.getRow())

    def getColumn(self):

        column = input("Enter column [A|B|C]: ")
        if (column.__eq__("A") or column.__eq__("B") or column.__eq__("C")):
            self.giveFeedback(Feedback.WRONG_INPUT)
            column = self.getColumn()

        return column

    def getRow(self):

        row = input("Enter row [1|2|3]: ")
        if (not (row.__eq__("1") or row.__eq__("2") or row.__eq__("3"))):
            self.giveFeedback(Feedback.WRONG_INPUT)
            row = self.getRow()

        return row

    def giveFeedback(self, feedback):

        if (isinstance(Feedback.PLACE_OCCUPIED, feedback)):
            print("Die Position ist bereits besetzt!")

        elif(isinstance(Feedback.WRONG_INPUT, feedback)):
            print("This is no valid input.\nPlease choose from the options between the braces.\n")

        elif(isinstance(Feedback.GAME_LOST, feedback)):
            print("You have won the game! :)")

        elif(isinstance(Feedback.GAME_WON, feedback)):
            print("You have lost the game. :/")

        elif(isinstance(Feedback.GAME_PAT, feedback)):
            print("The game is over and no one won.")


