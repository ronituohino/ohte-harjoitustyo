import unittest
from services.sudoku import Sudoku

# Test main Sudoku functionality


class TestSudoku(unittest.TestCase):
    def setUp(self):
        # Load a_start.sudoku from file before each test
        self.sudoku = Sudoku("test.sudoku")

    def test_sudoku_load(self):
        self.assertEqual(
            self.sudoku.grid,
            [
                2,
                1,
                9,
                5,
                4,
                3,
                6,
                7,
                8,
                5,
                4,
                3,
                8,
                7,
                6,
                9,
                1,
                2,
                8,
                7,
                6,
                2,
                1,
                9,
                3,
                4,
                5,
                4,
                3,
                2,
                7,
                6,
                5,
                8,
                9,
                1,
                7,
                6,
                5,
                0,
                0,
                8,
                2,
                3,
                4,
                1,
                9,
                8,
                4,
                3,
                0,
                5,
                6,
                7,
                3,
                2,
                1,
                6,
                5,
                4,
                7,
                8,
                9,
                6,
                5,
                4,
                9,
                8,
                7,
                1,
                2,
                3,
                9,
                8,
                7,
                3,
                2,
                1,
                4,
                5,
                6,
            ],
        )

    def test_sudoku_set_selection_value(self):
        self.sudoku.set_selection_value(5)
        self.assertEqual(self.sudoku.selection_value, 5)

    def test_sudoku_change_value(self):
        self.sudoku.set_selection_value(2)
        self.sudoku.set_value((5, 5))
        self.assertEqual(self.sudoku.grid[5 * 9 + 5], 2)

    def test_sudoku_solve(self):
        self.sudoku.set_selection_value(1)
        self.sudoku.set_value((3, 4))
        self.sudoku.set_selection_value(9)
        self.sudoku.set_value((4, 4))
        self.sudoku.set_selection_value(2)
        self.sudoku.set_value((5, 5))
        self.assertEqual(self.sudoku.solved, True)
