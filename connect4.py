# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:24:11 2018

@author: thomas
"""

class Connect4:
    board = [[]]
    def __init__(self):
        self.board = [[],[],[],[],[],[],[]]
    
    #turn is 1 for ai 0 for player
    def add_to_board(self, turn, column):
        if turn == True:
            self.board[column].append("O")
        else:
            self.board[column].append("X")
        return True
    
    def print_board(self):
        top = 5 
        line = ""
        for i in range(top, -1, -1):
            line = ""
            for j in range(7):
                if len(self.board[j]) <= i:
                    line += "_"
                else:                   
                    line += (self.board[j][i])
            print(line)
            
#########################################################################################