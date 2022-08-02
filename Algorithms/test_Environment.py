import unittest

from Environment import Board


class TestEnvironment(unittest.TestCase):
    def test_stringifyBoard(self):
        a1 = [[0, 1, 1, 2, 2, 2, 1], [0, 0, 2, 2, 2, 1, 0], [0, 0, 1, 1, 1, 2, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        a1Val = '0112221 0022210 0011120 0001000 0000000 0000000 ' 


        f = Board()
        self.assertEqual(f.stringifyBoard(f.currentBoard), '0000000 0000000 0000000 0000000 0000000 0000000 ')
        f.currentBoard = a1
        self.assertEqual(f.stringifyBoard(a1), a1Val)
    
    def test_stringToListBoard(self):
        
        a1Val = '0112221 0022210 0011120 0001000 0000000 0000000 ' 
        a1 = [[0, 1, 1, 2, 2, 2, 1], [0, 0, 2, 2, 2, 1, 0], [0, 0, 1, 1, 1, 2, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertCountEqual(Board.stringToListBoard(a1Val), a1)




if __name__ == '__main__':
    unittest.main()