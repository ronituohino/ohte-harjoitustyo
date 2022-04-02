import pygame
import os

pygame.init()
font = pygame.font.SysFont("comicsans", 40)


class Sudoku:
    def __init__(self, name):
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

        self.is_initialized = True

    def tick(self, screen, screen_dimensions):
        self.draw(screen, screen_dimensions)

    def handle_click(self, coords):
        pass

    def draw(self, screen, screen_dimensions):
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension/9

        # Draw numbered squares
        for y in range(9):
            for x in range(9):
                number = self.grid[y*9+x]
                if number != 0:
                    # Fill blue color in already numbered grid
                    pygame.draw.rect(screen, (100, 100, 100),
                                     (y * grid_size, x * grid_size, grid_size + 1, grid_size + 1))

                    # Fill grid with default numbers specified
                    text = font.render(str(number), 1, (0, 0, 0))
                    screen.blit(text, (y * grid_size + grid_size /
                                2, x * grid_size + grid_size/2))

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
