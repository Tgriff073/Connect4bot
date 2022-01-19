# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:25:13 2018

@author: thomas
Description: class is used to define what a game consists of, it will control the flow of the game
and perform functions like start the game, get user moves, and get ai moves.
a game object consists of a connect4 object(which is essentially just the board) a boolean that determines whether
the 2nd player is ai or not(currently ai move is random but eventually ai moves will be determined by MIN-MAX tree 
and alpha beta pruining to reduce the search space). 
"""

import numpy as np
#########################################################################################   
class Game:
    def __init__(self, board):
        self.board = board
        self.cpu_game = False
        self.turn = 0
    
##############################################################
    
    def start_game(self):
        #getting initial input is looped so that a valid option is selected.
        while True:
            choice = input("(S)ingle player or (M)ultiplayer? *Enter S for single player or M for multiplayer then press enter*:\n")
            choice = choice.capitalize()
            #exit the loop if the user enters "m" and state that the 2nd player wont be an AI
            if choice == "M":
                self.cpu_game = False
                break
            #exit the loop if the user enters "s" and state that the 2nd player will be an AI 
            elif choice == "S": 
                self.cpu_game = True
                break
            #otherwise display an error message and get the user input again
            else:
                print("INVALID INPUT (Please enter either m or s)\n\n")
        
        
##############################################################
                
    def run_game(self):
        #while there are still available slots (there is only a possibilty of 42 valid turns) get either 
        #the player move or AI move, then print the board. 
        while self.turn < 42:
            self.get_move()
            self.board.print_board()
        print ("Game over!")
##############################################################
         
    def get_move(self):
        #if the turn number is odd and its a cpu_game then call the ai function 
        #to get the next move, otherwise get the input from the user
        if self.turn%2 == 1 and self.cpu_game == True:
            move = self.get_ai_move()
            print(f"\nAI is moving to {move}")
        else:
            move = self.get_player_move()
        self.board.add_to_board(self.turn%2, move)
        self.turn += 1
##############################################################      

    def get_ai_move(self):
       while True:
           move = np.random.randint(0,7)
           if self.is_valid(move):
               return move
##############################################################    
               
    def get_player_move(self):
        #loop till the user enters a valid row, IE between 0 and 6 and the column isnt full
        while True:
            move = self.get_input()
            if self.is_valid(move):        
                return move
                break
            else:
                print("INVALID MOVE\n\n")
##############################################################   
                
    def is_valid(self, column):
        #if the column passed as an arg isnt between 0 and 6 or the column is full
        #return false
        if column > 6 or column < 0 or len(self.board.board[column]) == 6:
            return False
        #otherwise return true
        else:
            return True
        
##############################################################  
    def check_win(self, move):
        win = self.check_diagonal_win(move) or self.check_horizontal_win(move) or self.check_diagonal_win(move)
        return win

##############################################################  
    def get_input(self):
        return int(input("What column would you like to move to?"))
##############################################################  
    def check_vertical_win(self, move):
        if(len(self.board.board[move]) < 4):
            return False
        row_num = len(self.board.board[move]) - 1
        last_played_piece = self.board.board[move][row_num]
        for i in range (row_num, row_num - 4, -1):
            if self.board.board[move][i] != last_played_piece:
                return False
        return True
############################################################## 
    def check_horizontal_win(self, move):
        row_num = len(self.board.board[move]) - 1
        initial_char = self.board.board[move][row_num]
        for i in range (move-3, move+1):
            current_chain = 0
            if i < 0 or i > 6:
                continue
            for j in range(i, i +4):
                if  j > 6 or len(self.board.board[j]) < len(self.board.board[move]):
                    break
                if self.board.board[j][row_num] == initial_char:
                    current_chain += 1
                else:
                    current_chain = 0 
                    break
                if current_chain == 4:
                    return True
        return False
    def check_diagonal_win(self, move):
        neg_diagonal_result = self.check_neg_diagonal_win(move)
        pos_diagonal_result = self.check_pos_diagonal_win(move)
        return neg_diagonal_result or pos_diagonal_result
    def check_pos_diagonal_win(self, move):
        y1 = len(self.board.board[move]) - 1
        x1 = move
        x = move - 3
        y = y1 - 3
        initial_char = self.board.board[x1][y1]
        print(y)
        current_chain = 0
        for i in range(0, 7):
            if current_chain == 4:
                return True
            if i + y < 0 or i + y > 5 or i + x < 0 or i + x > 6 or len(self.board.board[x+i]) - 1 < y + i: 
                current_chain = 0
                continue
            if self.board.board[x+i][y+i] == initial_char:
                current_chain += 1
        return current_chain == 4
    def check_neg_diagonal_win(self, move):
        y1 = len(self.board.board[move]) - 1
        x1 = move
        x = move - 3
        y = y1 + 3
        initial_char = self.board.board[x1][y1]
        print(y)
        current_chain = 0
        for i in range(0, 7):
            if current_chain == 4:
                return True
            if y - i < 0 or y - i > 5 or x + i < 0 or x + i > 6 or len(self.board.board[x+i]) - 1 < y-i: 
                current_chain = 0
                continue
            if self.board.board[x+i][y-i] == initial_char:
                current_chain += 1
        return current_chain == 4
            