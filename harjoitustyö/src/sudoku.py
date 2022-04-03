import pygame
import os
from button import Button

# Sudoku Game handler


class Sudoku:
    def __init__(self, name: str) -> None:
        cwd = os.getcwd()
        file = open(f"{cwd}/sudokus/{name}", "r")

        # Read the .sudoku file
        string = ""
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

    # When using game UI, this must be called after class init
    def init_ui(self, canvas: "Canvas", screen_dimensions: list) -> None:
        # Init UI elements
        self.sudoku_buttons = [None] * (9*9)
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension/11
        for y in range(9):
            for x in range(9):
                self.sudoku_buttons[y*9+x] = Button(canvas, (100, 100, 100), x*grid_size, y*grid_size,
                                                    grid_size+1, grid_size+1, str(self.grid[y*9+x]), int(grid_size), None, self.set_value, (x, y))

        self.number_buttons = [None] * 9
        for i in range(9):
            self.number_buttons[i] = Button(canvas, (100, 100, 100), 10*grid_size,
                                            i*grid_size, grid_size, grid_size, str(i+1), int(grid_size), ((0, 0, 0), 3), self.set_selection_value, i+1)

    # Set value in sudoku board to selection_value
    def set_value(self, coords: tuple) -> None:
        self.grid[coords[1] * 9 + coords[0]] = self.selection_value

        # Also check if the Sudoku is solved now
        self.solved = self.check_sudoku()

    # Set the selection value
    def set_selection_value(self, value: int) -> None:
        self.selection_value = value

    def check_sudoku(self) -> bool:
        horizontal_rows = [self.grid[i*9:i*9+9] for i in range(9)]
        vertical_rows = [self.grid[i:9*9+i:9] for i in range(9)]

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
            has_num[num-1] = True

        # This returns False, if one of has_num is False
        return min(has_num)

    # Game UI functions
    # tick is called once per frame

    def tick(self, screen, screen_dimensions: list) -> None:
        self.draw(screen, screen_dimensions)

    def draw(self, screen, screen_dimensions: list) -> None:
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension/11

        # Draw numbered squares
        for y in range(9):
            for x in range(9):
                value = self.grid[y*9+x]
                button = self.sudoku_buttons[y*9+x]
                button.update_text(str(self.grid[y*9+x]))
                button.update_position(x*grid_size, y*grid_size)
                button.update_size(grid_size+1, grid_size+1)
                button.update_font_size(int(grid_size))
                if value > 0:
                    button.draw(screen)

        # Draw lines horizontally and vertically to form grid
        for i in range(10):
            # Varying thickness
            if i % 3 == 0:
                thickness = 6
            else:
                thickness = 1

            pygame.draw.line(screen, (0, 0, 0), (0, i * grid_size),
                             (grid_size * 9, i * grid_size), thickness)
            pygame.draw.line(screen, (0, 0, 0), (i * grid_size, 0),
                             (i * grid_size, grid_size * 9), thickness)

        # Draw number selection buttons
        for i in range(9):
            button = self.number_buttons[i]
            button.update_position(10*grid_size, i*grid_size)
            button.update_size(grid_size, grid_size)
            button.update_font_size(int(grid_size))
            button.draw(screen)

        if self.solved:
            font = pygame.font.SysFont('comicsans', int(grid_size))
            text = font.render("Congratulations!", 1, (0, 0, 0))
            screen.blit(text, (0, grid_size * 10))
