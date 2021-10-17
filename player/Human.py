from player.Feedback import Feedback
from player.Player import Player

class Human(Player):

    def makeMove(self, board):

        print(board)
        return Position(self.getColumn(), self.getRow())

    def getColumn(self):

        column = input("Enter column [A|B|C]: ")
        if column.__eq__("a") or column.__eq__("A"):
            return 0
        elif column.__eq__("b") or column.__eq__("B"):
            return 1
        elif column.__eq__("c") or column.__eq__("C"):
            return 2
        else:
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

        if Feedback.PLACE_OCCUPIED == feedback:
            print("Die Position ist bereits besetzt!")

        elif Feedback.WRONG_INPUT == feedback:
            print("This is no valid input.\nPlease choose from the options between the braces.\n")

        elif Feedback.GAME_LOST == feedback:
            print("You have lost the game. :/")

        elif Feedback.GAME_WON == feedback:
            print("You have won the game! :)")

        elif Feedback.GAME_DRAW == feedback:
            print("The game is over and no one won.")