import os
import pygame
from ui.button import Button
from ui.view import View

from services.sudoku import Sudoku

# Sudoku Game view


class SudokuView(View):
    def __init__(self, canvas: "Canvas", name: str) -> None:
        self.sudoku = Sudoku(name)

        # Init UI elements
        self.sudoku_buttons = [None] * (9 * 9)
        smaller_dimension = min(canvas.screen_dimensions)
        grid_size = smaller_dimension / 11
        for i in range(9):
            for j in range(9):
                self.sudoku_buttons[i * 9 + j] = Button(
                    canvas,
                    (100, 100, 100),
                    j * grid_size,
                    i * grid_size,
                    grid_size + 1,
                    grid_size + 1,
                    str(self.sudoku.grid[i * 9 + j]),
                    int(grid_size),
                    None,
                    self.sudoku.set_value,
                    (j, i),
                )

        self.number_buttons = [None] * 9
        for i in range(9):
            self.number_buttons[i] = Button(
                canvas,
                (100, 100, 100),
                10 * grid_size,
                i * grid_size,
                grid_size,
                grid_size,
                str(i + 1),
                int(grid_size),
                ((0, 0, 0), 3),
                self.sudoku.set_selection_value,
                i + 1,
            )

    # Game UI functions
    # tick is called once per frame

    def tick(self, screen, screen_dimensions: list) -> None:
        self.draw(screen, screen_dimensions)

    def draw(self, screen, screen_dimensions: list) -> None:
        smaller_dimension = min(screen_dimensions)
        grid_size = smaller_dimension / 11

        self.draw_sudoku_buttons(screen, grid_size)
        self.draw_sudoku_grid(screen, grid_size)
        self.draw_number_selection(screen, grid_size)
        self.draw_success_message(screen, grid_size)

    def draw_sudoku_buttons(self, screen, grid_size):
        # Draw numbered squares
        for i in range(9):
            for j in range(9):
                value = self.sudoku.grid[i * 9 + j]
                button = self.sudoku_buttons[i * 9 + j]
                button.update_text(str(self.sudoku.grid[i * 9 + j]))
                button.update_position(j * grid_size, i * grid_size)
                button.update_size(grid_size + 1, grid_size + 1)
                button.update_font_size(int(grid_size))
                if value > 0:
                    button.draw(screen)

    def draw_sudoku_grid(self, screen, grid_size):
        # Draw lines horizontally and vertically to form grid
        for i in range(10):
            # Varying thickness
            if i % 3 == 0:
                thickness = 6
            else:
                thickness = 1

            pygame.draw.line(
                screen,
                (0, 0, 0),
                (0, i * grid_size),
                (grid_size * 9, i * grid_size),
                thickness,
            )
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (i * grid_size, 0),
                (i * grid_size, grid_size * 9),
                thickness,
            )

    def draw_number_selection(self, screen, grid_size):
        # Draw number selection buttons
        for i in range(9):
            button = self.number_buttons[i]
            button.update_position(10 * grid_size, i * grid_size)
            button.update_size(grid_size, grid_size)
            button.update_font_size(int(grid_size))
            button.draw(screen)

    def draw_success_message(self, screen, grid_size):
        if self.sudoku.solved:
            font = pygame.font.SysFont("comicsans", int(grid_size))
            text = font.render("Congratulations!", 1, (0, 0, 0))
            screen.blit(text, (0, grid_size * 10))
