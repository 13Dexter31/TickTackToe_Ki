#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Board import Board
from Board import Result


# In[ ]:


class Game:
    
    # TODO 2-3 tests implementieren

    def __init__(self, players=[]):
        self.players = players

    def turn(self,player,board):
        position = player.makeMove(board)
        is_valid = board.update(position, player)
        if not is_valid:
            new_try = False
            while not new_try:
                player.feedback(Result.INVALID_MOVE)
                col,row = player.makeMove(board)
                new_try = board.update(col,row, player)

    def start(self):
        board = Board()
        state = Result.NO_RESULT
        # loop till the game does not continue
        while state == Result.NO_RESULT:
            for player in self.players:
                # current player makes a move
                self.turn(player,board)
                # check if game is over
                state = board.over()
                # check if the player won or drawed
                if state == Result.GAME_WON:
                    # if he is the winner, everyone else is the looser
                    for looser in self.players:
                        # send state to the looser
                        if not looser == player:
                            looser.feedback(Result.GAME_LOST)
                    # send state to the winner£
                    player.feedback(state)
                    break
                elif state == Result.DRAW:
                    # send state to all players that it's a draw
                    for playerDraw in self.players:
                        playerDraw.feedback(state)
                    break

