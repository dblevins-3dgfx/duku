import unittest
from duku import Square
from duku import Duku

class TestSquare(unittest.TestCase):

    def test_square_init(self):
        sq = Square(0, 0)
        self.assertEqual(sq.value, None)
        self.assertEqual(sq.coord, (0, 0))

class TestDuku(unittest.TestCase):
    def setUp(self):
        self.game = Duku()

    def test_duku_init(self):
        self.assertTrue(isinstance(self.game.board, list))
        self.assertEqual(len(self.game.board), 9)
        self.assertTrue(isinstance(self.game.board[0], list))
        self.assertEqual(len(self.game.board[0]), 9)
        self.assertEqual(self.game.board[0][0].value, None)
        self.assertEqual(self.game.board[0][0].coord, (0,0))
        self.assertEqual(self.game.board[0][8].value, None)
        self.assertEqual(self.game.board[0][8].coord, (0,8))
        self.assertEqual(self.game.board[8][0].value, None)
        self.assertEqual(self.game.board[8][0].coord, (8,0))
        self.assertEqual(self.game.board[8][8].value, None)
        self.assertEqual(self.game.board[8][8].coord, (8,8))

    def test_duku_fillboard(self):
        self.game.fill_fixed()
        self.assertEqual(self.game.board[0][0].value, 1)
        self.assertEqual(self.game.board[0][8].value, 9)
        self.assertEqual(self.game.board[1][0].value, 4)
        self.assertEqual(self.game.board[1][8].value, 3)

    def test_row_values(self):
        self.assertListEqual(self.game.row_values(0), [])
        self.game.sequentialize_row(self.game.board[0], 0)
        self.assertListEqual(self.game.row_values(0), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_col_values(self):
        self.assertListEqual(self.game.col_values(0), [])
        self.game.fill_fixed()
        self.assertListEqual(self.game.col_values(0), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    def test_block_values(self):
        self.assertListEqual(self.game.block_values((0, 0)), [])
        self.game.fill_fixed()
        self.assertListEqual(self.game.block_values((0,0)), [1, 2, 3, 4, 5, 6, 7, 8, 9])


    def test_legal_empty_state(self):
        self.assertTrue(self.game.check_unique(self.game.row_values(0)))
        self.assertTrue(self.game.check_unique(self.game.col_values(0)))
        self.assertTrue(self.game.check_unique(self.game.block_values((0,0))))
        self.assertTrue(self.game.check_legal())

    def test_legal_filled_state(self):
        self.game.fill_fixed()
        self.assertTrue(self.game.check_unique(self.game.row_values(0)))
        self.assertTrue(self.game.check_unique(self.game.col_values(0)))
        self.assertTrue(self.game.check_unique(self.game.block_values((0,0))))

    def test_illegal_row_state(self):
        self.game.fill_fixed()
        self.game.board[0][1].value = self.game.board[0][0].value
        self.game.board[1][0].value = self.game.board[0][0].value
        self.assertFalse(self.game.check_unique(self.game.row_values(0)))
        self.assertFalse(self.game.check_unique(self.game.col_values(0)))
        self.assertFalse(self.game.check_unique(self.game.block_values((0,0))))

    def test_is_complete(self):
        self.assertFalse(self.game.is_complete())
        self.game.fill_fixed();
        self.assertTrue(self.game.is_complete())

if __name__ == '__main__':
    unittest.main()