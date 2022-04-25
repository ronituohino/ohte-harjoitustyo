import os
from os.path import isfile, join


class Menu:
    def __init__(self, game, sudoku_folder_path):
        self.game = game

        self.sudokus = [
            f
            for f in os.listdir(sudoku_folder_path)
            if isfile(join(sudoku_folder_path, f))
        ]
        self.selected_sudoku = 0
        self.sudoku_amount = len(self.sudokus)

    def __name__(self):
        return "Menu"

    def move_left(self):
        if self.selected_sudoku > 0:
            self.selected_sudoku -= 1

    def move_right(self):
        if self.selected_sudoku < self.sudoku_amount - 1:
            self.selected_sudoku += 1

    def open_sudoku(self):
        self.game.open_sudoku(self.sudokus[self.selected_sudoku])

    def open_login(self):
        self.game.open_login()

    def logout(self):
        self.game.logout()
