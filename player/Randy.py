#!/usr/bin/env python
# coding: utf-8

# In[21]:


from random import randint
from player.Player import Player


class Randy(Player):

    def makeMove(self, board):
        return randint(1, 3), randint(1, 3)

    def giveResult(self, result):
        pass

