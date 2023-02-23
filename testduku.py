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

    def test_row_values(self):
        game = Duku()
        self.assertListEqual(game.row_values(0), [])
        game.sequentialize_row(game.board[0], 0)
        self.assertListEqual(game.row_values(0), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_col_values(self):
        game = Duku()
        self.assertListEqual(game.col_values(0), [])
        game.fillboard()
        self.assertListEqual(game.col_values(0), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    def test_block_values(self):
        game = Duku()
        self.assertListEqual(game.block_values((0, 0)), [])
        game.fillboard()
        self.assertListEqual(game.block_values((0,0)), [1, 2, 3, 4, 5, 6, 7, 8, 9])


    def test_legal_empty_state(self):
        game = Duku()
        self.assertTrue(game.check_unique(game.row_values(0)))
        self.assertTrue(game.check_unique(game.col_values(0)))
        self.assertTrue(game.check_unique(game.block_values((0,0))))
        self.assertTrue(game.check_legal())

    def test_legal_filled_state(self):
        game = Duku()
        game.fillboard()
        self.assertTrue(game.check_unique(game.row_values(0)))
        self.assertTrue(game.check_unique(game.col_values(0)))
        self.assertTrue(game.check_unique(game.block_values((0,0))))

    def test_illegal_row_state(self):
        game = Duku()
        game.fillboard()
        game.board[0][1].value = game.board[0][0].value
        game.board[1][0].value = game.board[0][0].value
        self.assertFalse(game.check_unique(game.row_values(0)))
        self.assertFalse(game.check_unique(game.col_values(0)))
        self.assertFalse(game.check_unique(game.block_values((0,0))))

if __name__ == '__main__':
    unittest.main()