#!/usr/bin/env python
# coding: utf-8

# In[1]:


from abc import abstractmethod

class Player():

    def __init__(self, representationChar) -> None:
        self.representationChar = representationChar

    def __str__(self):
        return self.representationChar

    @abstractmethod
    def makeMove(self, board):
        pass

    @abstractmethod
    def giveResult(self, result):
        pass

