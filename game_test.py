import unittest
from unittest.mock import patch
from game import Game
from connect4 import Connect4
import pytest


class IsValid(unittest.TestCase):
    def test_is_valid_full_column(self):
        board = Connect4()
        for i in range(0, 6):
            board.add_to_board(0, 2)
        game = Game(board)

        result = game.is_valid(2)

        self.assertEqual(result, False)

    def test_is_valid_empty_column(self):
        board = Connect4()
        game = Game(board)

        result = game.is_valid(4)

        self.assertEqual(result, True)

    def test_is_valid_invalid_column(self):
        board = Connect4()
        game = Game(board)

        result = game.is_valid(7)

        self.assertEqual(result, False)

    def test_is_valid_negative_column(self):
        board = Connect4()
        game = Game(board)

        result = game.is_valid(-4)

        self.assertEqual(result, False)

class GetMove(unittest.TestCase):
    @patch('game.Game.get_input', return_value=5)
    def test_get_move_user(self, input):
        board = Connect4()
        game = Game(board)

        game.get_move()

        self.assertEqual(game.board.board[5][0], 'X')

    @patch('numpy.random.randint', return_value=3)
    def test_get_move_bot(self, random):
        board = Connect4()
        game = Game(board)
        game.turn = 1
        game.cpu_game = True
        game.get_move()
        self.assertEqual(game.board.board[3][0], 'O')
class CheckWin(unittest.TestCase):
    def test_win_vertical(self):
        board = Connect4()
        for i in range(0,4):
            board.add_to_board(0, 1)
        game = Game(board)

        result = game.check_win(1)
        self.assertEqual(result, True)
    def test_win_horizontal(self):
        board = Connect4()
        for i in range(0,4):
            board.add_to_board(0, i)
        game = Game(board)

        result = game.check_win(1)
        self.assertEqual(result, True)
    def test_win_diagonal(self):
        board = Connect4()
        board.board = [['X','O'],['O','X','X'],['X'],['O','X','X'],['X','O','X'],['O','X','X','X'],['X','O','O']]
        game = Game(board)
        board.print_board()
        result = game.check_win(2)
        self.assertEqual(result, True)
class CheckVerticalWin(unittest.TestCase):
    def test_win(self):
        board = Connect4()
        for i in range(0,4):
            board.add_to_board(0, 1)
        game = Game(board)

        result = game.check_vertical_win(1)

        self.assertEqual(result, True)
    
    def test_4_in_column_but_bot_pieces_in_between(self):
        board = Connect4()
        for i in range(0,4):
            board.add_to_board(i%2, 1)
        board.print_board()
        game = Game(board)

        result = game.check_vertical_win(1)

        self.assertEqual(result, False)

    def test_less_than_4_pieces(self):
        board = Connect4()
        for i in range(0,3):
            board.add_to_board(0, 1)
        game = Game(board)

        result = game.check_vertical_win(1)

        self.assertEqual(result, False)
    
    def test_more_than_4_in_a_column_win(self):
        board = Connect4()
        for i in range(0,6):
            board.add_to_board(i<2, 1)
        game = Game(board)

        result = game.check_vertical_win(1)

        self.assertEqual(result, True)
class CheckHorizontalWin(unittest.TestCase):
    def test_win_horizontal(self):
        board = Connect4()
        for i in range(0,4):
            board.add_to_board(0, i)
        game = Game(board)

        result = game.check_horizontal_win(1)
        self.assertEqual(result, True)
    def test_3_horizontal(self):
        board = Connect4()
        for i in range(0,3):
            board.add_to_board(0, i)
        game = Game(board)

        result = game.check_horizontal_win(1)

        self.assertEqual(result, False)
    def test_3_horizontal(self):
        board = Connect4()
        for i in range(0,4):
            board.add_to_board(i%2, i)
        game = Game(board)

        result = game.check_horizontal_win(1)

        self.assertEqual(result, False)
    def test_win_horizontal_not_0_row(self):
        board = Connect4()
        board.board = [['X','O'],['O','X','X'],['X','O'],['O','X','X'],['X','O','X'],['O','X','X'],['X','O','O']]
        game = Game(board)

        result = game.check_horizontal_win(5)

        self.assertEqual(result, False)
class CheckDiagonalWin(unittest.TestCase):
    def test_win_pos_diagonal(self):
        board = Connect4()
        board.board = [['X','O'],['O','X','X'],['X'],['O','X','X'],['X','O','X'],['O','X','X','X'],['X','O','O']]
        game = Game(board)
        board.print_board()
        result = game.check_diagonal_win(2)
        self.assertEqual(result, True)
    def test_win_neg_diagonal(self):
        board = Connect4()
        board.board = [['X','O'],['O','X','X','X'],['X','O','X'],['O','X','X'],['X','O','X'],['O','X','X','X'],['X','O','O']]
        game = Game(board)
        board.print_board()
        result = game.check_diagonal_win(2)
        self.assertEqual(result, True)
    def test_no_win_diagonal(self):
        board = Connect4()
        board.board = [['X','O'],['O','X','X'],['X','O'],['O','X','X'],['X','O','X'],['O','X','X','X'],['X','O','O']]
        game = Game(board)
        board.print_board()
        result = game.check_diagonal_win(2)
        self.assertEqual(result, False)
if __name__ == '__main__':
    unittest.main()