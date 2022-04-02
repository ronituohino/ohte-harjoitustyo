import pygame
import os
from button import Button

pygame.init()
font = pygame.font.SysFont("comicsans", 40)

# Sudoku Game view


class Sudoku:
    def __init__(self, name, canvas, screen_dimensions):
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

        # Init UI elements
        self.sudoku_buttons = [None] * (9*9)
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension/11
        for y in range(9):
            for x in range(9):
                self.sudoku_buttons[y*9+x] = Button(canvas, (100, 100, 100), x*grid_size, y*grid_size,
                                                    grid_size+1, grid_size+1, str(self.grid[y*9+x]), None, self.set_value, (x, y))

        self.selection_value = 1
        self.number_buttons = [None] * 9
        for i in range(9):
            self.number_buttons[i] = Button(canvas, (100, 100, 100), 10*grid_size,
                                            i*grid_size, grid_size, grid_size, str(i+1), ((0, 0, 0), 3), self.set_selection_value, i+1)

    def tick(self, screen, screen_dimensions):
        self.draw(screen, screen_dimensions)

    def draw(self, screen, screen_dimensions):
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension/11

        # Draw numbered squares
        for y in range(9):
            for x in range(9):
                button = self.sudoku_buttons[y*9+x]
                button.update_text(str(self.grid[y*9+x]))
                button.update_position(x*grid_size, y*grid_size)
                button.update_size(grid_size+1, grid_size+1)
                button.draw(screen)

        # Draw lines horizontally and vertically to form grid
        for i in range(10):
            # Varying thickness
            if i % 3 == 0:
                thick = 6
            else:
                thick = 1

            pygame.draw.line(screen, (0, 0, 0), (0, i * grid_size),
                             (grid_size * 9, i * grid_size), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * grid_size, 0),
                             (i * grid_size, grid_size * 9), thick)

        # Draw number selection buttons
        for i in range(9):
            button = self.number_buttons[i]
            button.update_position(10*grid_size, i*grid_size)
            button.update_size(grid_size, grid_size)
            button.draw(screen)

    # Set value in sudoku board to selection_value
    def set_value(self, coords):
        self.grid[coords[1] * 9 + coords[0]] = self.selection_value

    # Set the selection value
    def set_selection_value(self, value):
        self.selection_value = value
