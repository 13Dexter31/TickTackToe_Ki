from player.Player import Player

class Human(Player):

    def getPosition(self):
        return Position(self.getColumn(), self.getRow())

    def getColumn(self):

        column = input("Enter column [A|B|C]: ")
        if (column.__eq__("A") or column.__eq__("B") or column.__eq__("C")):
            return column

    def getRow(self):

        row = input("Enter row [1|2|3]: ")
        if (row.__eq__("1") or row.__eq__("2") or row.__eq__("3")):
            return row

    def giveFeedback(self, feedback):

        if (isinstance(Feedback.PLACE_OCCUPIED, feedback)):