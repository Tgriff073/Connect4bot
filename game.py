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

from connect4 import Connect4
import numpy as np
#########################################################################################   
class Game:
    
    board = Connect4()
    cpu_game = False
    turn = 0
    
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
            move = int(input("What column would you like to move to?"))
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
        

#########################################################################################   