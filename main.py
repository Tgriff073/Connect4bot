# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:46:07 2018

@author: thomas
"""
import numpy as np

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
class Game:
    board = Connect4()
    cpu_game = False
    turn = 0
    def start_game(self):
        while True:
            choice = input("(S)ingle player or (M)ultiplayer? *Enter S for single player or M for multiplayer then press enter*:\n")
            choice = choice.capitalize()
            if choice == "M":
                self.cpu_game = False
                break
            elif choice == "S": 
                self.cpu_game = True
                break
            else:
                print("INVALID INPUT\n\n")
        while True:
            if self.turn >= 42:
                break
            self.get_move()
            self.board.print_board()
        print ("Game over!")
            
    def get_move(self):
        if self.turn%2 == 1 and self.cpu_game == True:
            move = self.get_ai_move()
            print(f"\nAI is moving to {move}")
        else:
            move = self.get_player_move()
        self.board.add_to_board(self.turn%2, move)
        self.turn += 1
        
    def get_ai_move(self):
       while True:
           move = np.random.randint(0,7)
           if self.is_valid(move):
               return move
    
    def get_player_move(self):
        while True:
            move = int(input("What column would you like to move to?"))
            if self.is_valid(move):        
                return move
                break
            else:
                print("INVALID MOVE\n\n")
                
    def is_valid(self, column):
        if column > 6 or column < 0 or len(self.board.board[column]) == 6:
            return False
        else:
            return True
        

#########################################################################################                    
def main():
    g = Game()
    g.start_game()
    
main()
    