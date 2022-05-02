import time
from utils.sudoku import parse_sudoku_file

# Sudoku -service


class Sudoku:
    def __init__(self, game, sudoku_folder_path, sudoku_name) -> None:
        self.game = game
        self.sudoku_name = sudoku_name
        self.time_start = time.time()
        self.completion_time = None

        string = parse_sudoku_file(sudoku_folder_path, sudoku_name)

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
        if self.check_sudoku():
            self.completion_time = time.time() - self.time_start

            # If logged in -> update database
            if self.game and self.game.user is not None:
                account_id = self.game.user["id"]
                self.game.database.add_completed(
                    account_id, self.sudoku_name, self.completion_time
                )

            # Update solved state
            self.solved = True

    # Set the selection value
    def set_selection_value(self, value: int) -> None:
        self.selection_value = value

    def check_sudoku(self) -> bool:
        horizontal_rows = [self.grid[i * 9: i * 9 + 9] for i in range(9)]
        vertical_rows = [self.grid[i: 9 * 9 + i: 9] for i in range(9)]

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

    def exit_to_menu(self):
        self.game.open_menu()
