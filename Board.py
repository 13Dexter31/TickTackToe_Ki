#!/usr/bin/env python
# coding: utf-8

# # Todo List
#     - konstruktor
#     - Methoden (update, over)
#     - Datenstruktur Spielfeld (2D-array)
#     - in over() Struktur winningConditions
#     - class result
#     - class position (pair)
#     - tests
#     
#     - __str__ (print weg)
#     - done Position Klasse weg (Indexing direkt in Klasse board(0,1))
#     - done nicht auf instance prüfen, stattdessen auf None
#     - DRY (schleifen)
#     - Spalte-Reihe 0,1,2 -> Docstring
# - GUI

# In[2]:


from enum import Enum

class Result(Enum):
    NO_RESULT = 0
    GAME_WON = 1
    GAME_LOST = 2
    GAME_DRAW = 3
    INVALID_MOVE = 4


# In[10]:


import numpy as np
from player.Player import Player

class Board:
    '''
    Contains attribute <field> (3x3 numpy array of type 'Player').
    The field can be accessed via the indices column and row.
    The indices can be in range 0..2.
    Example: board[0][1] will return the <Player> object in the center of the first column.
    
    Field: 00 10 20
           01 11 21
           02 12 22
    '''
    
    def __init__(self):       
        self.field = np.empty(shape=(3,3), dtype=Player)
    
    # String representation of the field
    def __str__(self):
        str_field = "{a1} | {b1} | {c1}\n{a2} | {b2} | {c2}\n{a3} | {b3} | {c3}"
        result = str_field.format(a1=self.field[0][0], b1=self.field[1][0], c1=self.field[2][0], 
                         a2=self.field[0][1], b2=self.field[1][1], c2=self.field[2][1], 
                         a3=self.field[0][2], b3=self.field[1][2], c3=self.field[2][2])
        return result
    
    # Allow Indexing from outside of the class
    def __getitem__(self, index):
        return self.field[index]
    
    # Update internal numpy array if column and row are valid
    # Parameter: - int column: Desired column on the board
    #            - int row: Desired row on the board
    #            - Player player: Currently active player
    def update(self, column, row, player):
        # check if row and column are valid
        if not((0 <= column <= 2) and (0 <= row <= 2)):
            return False
        
        # Check if desired position on board is empty
        if self.field[column][row] != None:
            return False
        
        self.markPlayer(column, row, player)
        return True
    
    # Fill in the currently active player in the numpy array at the desired column and row
    def markPlayer(self, column, row, player):
        self.field[column][row] = player
        
    # Check if a winning-condition has occured or if no more moves can be made
    # Returns Result (Currently returns the winning player, due to missing Player class)
    def over(self):   
        
        # Column winningconditions
        for col in range(3):
            if (self.field[col][0] == self.field[col][1] and self.field[col][0] == self.field[col][2]) and self.field[col][0] != None:
                return self.field[0][0]
        
        # Row winningconditions
        for row in range(3):
            if (self.field[0][row] == self.field[1][row] and self.field[0][row] == self.field[2][row]) and self.field[0][row] != None:
                return self.field[0][row]
        
        # Diagonal winningcondition
        if (self.field[0][0] == self.field[1][1] and self.field[0][0] == self.field[2][2]) and self.field[0][0] != None:
            return self.field[0][0]
        if (self.field[0][2] == self.field[1][1] and self.field[0][2] == self.field[2][0]) and self.field[0][2] != None:
            return self.field[0][2]
        
        # Draw
        if self.noMoreMoves():
            return Result.GAME_DRAW
        return Result.NO_RESULT
    
    # Check if no more moves can be made
    # Returns bool
    def noMoreMoves(self):
        for col, row in np.ndindex(self.field.shape):
            if self.field[col][row] == None:
                return False
        return True


# In[5]:


# Temporary Player class until final class is implemented
#class Player:
    #def __init__(self, _playerNumber):
     #   self.playerNumber = _playerNumber
        
    #def __str__(self):
     #   return str(self.playerNumber)


# In[6]:


if __name__ == "__main__":
    board = Board()
    player1 = Player(1)
    player2 = Player(2)

    board.update(0, 0, player1)
    board.update(1, 0, player2)
    board.update(2, 0, player1)
    board.update(0, 1, player2)
    board.update(1, 1, player1)
    board.update(2, 1, player2)
    board.update(0, 2, player1)
    board.update(1, 2, player2)
    board.update(2, 2, player1)
    print(board)


# In[7]:


if __name__ == "__main__":
    board = Board()
    print(board.__doc__)


# In[7]:


import ipywidgets as widgets
from IPython.display import display


# In[8]:


if __name__ == "__main__":
    board = Board()
    player1 = Player(1)
    player2 = Player(2)

    a1 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    b1 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    c1 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    row1 = [a1, b1, c1]
    HBox_1 = widgets.HBox(row1)

    a2 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    b2 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    c2 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    row2 = [a2, b2, c2]
    HBox_2 = widgets.HBox(row2)

    a3 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    b3 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    c3 = widgets.Dropdown(
        options=['None', 'X', 'O'],
        value='None',
        disabled=False,
        layout=widgets.Layout(width='80px'),
    )
    row3 = [a3, b3, c3]
    HBox_3 = widgets.HBox(row3)

    rows = [HBox_1, HBox_2, HBox_3]


    vBox = widgets.VBox(rows)
    button = widgets.Button(description='Done')
    inputs = [a1, a2, a3, b1, b2, b3, c1, c2, c3]

    def onclick(self):
        for i in inputs:
            if(i.disabled == False and i.value != "None"):
                i.disabled = True
                if(i.value == "X"):
                    player = player1
                else:
                    player = player2

                if(i == a1):
                    board.update(0, 0, player)
                elif(i == a2):
                    board.update(0, 1, player)
                elif(i == a3):
                    board.update(0, 2, player)
                elif(i == b1):
                    board.update(1, 0, player)
                elif(i == b2):
                    board.update(1, 1, player)
                elif(i == b3):
                    board.update(1, 2, player)
                elif(i == c1):
                    board.update(2, 0, player)
                elif(i == c2):
                    board.update(2, 1, player)
                elif(i == c3):
                    board.update(2, 2, player)
        result = board.over()
        if(result == player1):
            print("Player 1 won")
        elif(result == player2):
            print("Player 2 won")
        else:
            print(result)
    button.on_click(onclick)
    display(vBox)
    display(button)


# In[ ]:




