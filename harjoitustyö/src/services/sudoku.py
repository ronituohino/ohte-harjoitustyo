import os

# Sudoku -service


class Sudoku:
    def __init__(self, name: str, game) -> None:
        self.game = game

        # Read the .sudoku file
        string = ""
        cwd = os.getcwd()
        with open(f"{cwd}/sudokus/{name}", "r", encoding="utf8") as file:
            i = 0
            for line in file:
                if i < 12:
                    string += line

        # Turn the file into string of numbers
        string = string.replace("|", "")
        string = string.replace(",", "")
        string = string.replace("-", "")
        string = string.replace("\n", "")

        # Init board data
        self.grid = [int(c) for c in string]
        self.selection_value = 1
        self.solved = False

    def __name__(self):
        return "Sudoku"

    # Set value in sudoku board to selection_value
    def set_value(self, coords: tuple) -> None:
        self.grid[coords[1] * 9 + coords[0]] = self.selection_value

        # Also check if the Sudoku is solved now
        self.solved = self.check_sudoku()

    # Set the selection value
    def set_selection_value(self, value: int) -> None:
        self.selection_value = value

    def check_sudoku(self) -> bool:
        horizontal_rows = [self.grid[i * 9 : i * 9 + 9] for i in range(9)]
        vertical_rows = [self.grid[i : 9 * 9 + i : 9] for i in range(9)]

        for row in horizontal_rows:
            if not self.check_row(row):
                return False

        for row in vertical_rows:
            if not self.check_row(row):
                return False

        return True

    # Checks if a row has all of the numbers from 1-9
    def check_row(self, row: list) -> bool:
        has_num = [False] * 9
        for num in row:
            has_num[num - 1] = True

        # This returns False, if one of has_num is False
        return min(has_num)
