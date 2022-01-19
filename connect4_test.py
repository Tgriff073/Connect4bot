import unittest
from connect4 import Connect4
class Connect4Tests(unittest.TestCase):
  
    def test_user_place(self):        
        c4 = Connect4()
        c4.add_to_board(0, 1)
        self.assertEqual(c4.board[1][0], 'X')

    def test_bot_place(self):
        c4 = Connect4()
        c4.add_to_board(1, 5)
        self.assertEqual(c4.board[5][0], 'O')
  
if __name__ == '__main__':
    unittest.main()