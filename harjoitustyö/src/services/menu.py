from utils.sudoku import sudokus_in_folder


class Menu:
    def __init__(self, game, sudoku_folder_path):
        self.game = game

        self.sudokus = sudokus_in_folder(sudoku_folder_path)
        self.selected_sudoku = 0
        self.sudoku_amount = len(self.sudokus)

        if self.game is not None and self.game.user is not None:
            self.completed_data = self.get_completed_data()
            self.completed_sudokus = [t[0] for t in self.completed_data]
        else:
            self.completed_data = []
            self.completed_sudokus = []

    def get_completed_data(self):
        return self.game.database.get_completed_data(self.game.user["id"])

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
        self.completed_data = []
        self.completed_sudokus = []
        self.game.logout()
