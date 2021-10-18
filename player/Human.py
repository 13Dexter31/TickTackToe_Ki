#!/usr/bin/env python
# coding: utf-8

# In[6]:


from player.Player import Player
from Board import Result

class Human(Player):

    def makeMove(self, board):

        print(board)
        return self.getColumn(), self.getRow()

    def getColumn(self):

        column = input("Enter column [A|B|C]: ")
        if column.__eq__("a") or column.__eq__("A"):
            return 0
        elif column.__eq__("b") or column.__eq__("B"):
            return 1
        elif column.__eq__("c") or column.__eq__("C"):
            return 2
        else:
            self.giveResult(Result.WRONG_INPUT)
            column = self.getColumn()

        return column

    def getRow(self):

        row = input("Enter row [1|2|3]: ")
        if (not (row.__eq__("1") or row.__eq__("2") or row.__eq__("3"))):
            self.giveResult(Result.WRONG_INPUT)
            row = self.getRow()

        return row

    def giveResult(self, result):

        if Result.INVALID_MOVE == result:
            print("Die Position ist bereits besetzt!")

        elif Result.WRONG_INPUT == result:
            print("This is no valid input.\nPlease choose from the options between the braces.\n")

        elif Result.GAME_LOST == result:
            print("You have lost the game. :/")

        elif Result.GAME_WON == result:
            print("You have won the game! :)")

        elif Result.GAME_DRAW == result:
            print("The game is over and no one won.")

