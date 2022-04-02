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

        # Initialize board data
        self.grid = [int(x) for x in string]
        self.buttons = [None] * (9*9)
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension/9
        for y in range(9):
            for x in range(9):
                self.buttons[y*9+x] = Button(canvas, (100, 100, 100), x*grid_size, y*grid_size,
                                             grid_size+1, grid_size+1, str(self.grid[y*9+x]), self.set_value, (x, y), 1)

        self.is_initialized = True

    def tick(self, screen, screen_dimensions):
        self.draw(screen, screen_dimensions)

    def draw(self, screen, screen_dimensions):
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension/9

        # Draw numbered squares
        for y in range(9):
            for x in range(9):
                button = self.buttons[y*9+x]
                button.update_text(str(self.grid[y*9+x]))
                button.update_position(x*grid_size, y*grid_size)
                button.update_size(grid_size+1, grid_size+1)
                button.draw(screen)

        # Draw lines horizontally and vertically to form grid
        for y in range(10):
            # Varying thickness
            if y % 3 == 0:
                thick = 7
            else:
                thick = 1

            pygame.draw.line(screen, (0, 0, 0), (0, y * grid_size),
                             (smaller_dimension, y * grid_size), thick)
            pygame.draw.line(screen, (0, 0, 0), (y * grid_size, 0),
                             (y * grid_size, smaller_dimension), thick)

    def set_value(self, coords, value):
        self.grid[coords[1] * 9 + coords[0]] = value
