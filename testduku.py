import unittest
from duku import Square
from duku import Duku

class TestSquare(unittest.TestCase):

    def test_square_init(self):
        sq = Square(0, 0)
        self.assertEqual(sq.value, None)
        self.assertEqual(sq.coord, (0, 0))

class TestDuku(unittest.TestCase):

    def test_duku_init(self):
        game = Duku()
        self.assertTrue(isinstance(game.board, list))
        self.assertEqual(len(game.board), 9)
        self.assertTrue(isinstance(game.board[0], list))
        self.assertEqual(len(game.board[0]), 9)
        self.assertEqual(game.board[0][0].value, None)
        self.assertEqual(game.board[0][0].coord, (0,0))
        self.assertEqual(game.board[0][8].value, None)
        self.assertEqual(game.board[0][8].coord, (0,8))
        self.assertEqual(game.board[8][0].value, None)
        self.assertEqual(game.board[8][0].coord, (8,0))
        self.assertEqual(game.board[8][8].value, None)
        self.assertEqual(game.board[8][8].coord, (8,8))

    def test_duku_fillboard(self):
        game = Duku()
        game.fillboard()
        self.assertEqual(game.board[0][0].value, 1)
        self.assertEqual(game.board[0][8].value, 9)
        self.assertEqual(game.board[1][0].value, 4)
        self.assertEqual(game.board[1][8].value, 3)


if __name__ == '__main__':
    unittest.main()