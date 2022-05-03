import unittest
import os

from services.menu import Menu


class FakeGame:
    def __init__(self):
        self.user = None
        self.last_sudoku_opened = None
        self.open_sudoku_called = 0
        self.open_login_called = 0
        self.logout_called = 0

    def open_sudoku(self, sudoku):
        self.last_sudoku_opened = sudoku
        self.open_sudoku_called += 1

    def open_login(self):
        self.open_login_called += 1

    def logout(self):
        self.logout_called += 1


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu(FakeGame(), f"{os.getcwd()}/src/tests/test_sudokus")

    def test_sudoku_read(self):
        self.assertEqual(self.menu.sudoku_amount, 2)

    def test_move_right(self):
        self.menu.move_right()
        self.assertEqual(self.menu.selected_sudoku, 1)

    def test_move_left(self):
        self.menu.move_right()
        self.menu.move_left()
        self.assertEqual(self.menu.selected_sudoku, 0)

    def test_open_login(self):
        self.menu.open_login()
        self.assertEqual(self.menu.game.open_login_called, 1)

    def test_logout(self):
        self.menu.logout()
        self.assertEqual(self.menu.game.logout_called, 1)

    def test_open_sudoku(self):
        self.menu.open_sudoku()
        self.assertEqual(self.menu.game.last_sudoku_opened, "test2")
