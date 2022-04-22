import os
import pygame
from ui.components.button import Button
from ui.view import View
from services.sudoku import Sudoku

# Sudoku Game view


class SudokuView(View):
    def __init__(self, canvas: "Canvas", sudoku) -> None:
        self.canvas = canvas
        self.sudoku = sudoku

        # Init UI elements
        self.sudoku_buttons = [None] * (9 * 9)
        x_size, y_size = canvas.screen_dimensions
        grid_size = self.canvas.lower_screen_dimension / 11
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

        self.exit_button = Button(
            canvas,
            (255, 0, 0),
            x_size - self.canvas.lower_screen_dimension * 0.1,
            0,
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
            "exit",
            self.canvas.font_size,
            None,
            self.sudoku.exit_to_menu,
        )

    # Game UI functions
    # tick is called once per frame

    def tick(self) -> None:
        self.draw()

    def draw(self) -> None:
        x_size, y_size = self.canvas.screen_dimensions
        grid_size = self.canvas.lower_screen_dimension / 11

        self.draw_sudoku_buttons(grid_size)
        self.draw_sudoku_grid(grid_size)
        self.draw_number_selection(grid_size)
        self.draw_success_message(grid_size)
        self.draw_exit_button(x_size)

    def draw_sudoku_buttons(self, grid_size):
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
                    button.draw()

    def draw_sudoku_grid(self, grid_size):
        # Draw lines horizontally and vertically to form grid
        for i in range(10):
            # Varying thickness
            if i % 3 == 0:
                thickness = 6
            else:
                thickness = 1

            pygame.draw.line(
                self.canvas.screen,
                (0, 0, 0),
                (0, i * grid_size),
                (grid_size * 9, i * grid_size),
                thickness,
            )
            pygame.draw.line(
                self.canvas.screen,
                (0, 0, 0),
                (i * grid_size, 0),
                (i * grid_size, grid_size * 9),
                thickness,
            )

    def draw_number_selection(self, grid_size):
        # Draw number selection buttons
        for i in range(9):
            button = self.number_buttons[i]
            button.update_position(10 * grid_size, i * grid_size)
            button.update_size(grid_size, grid_size)
            button.update_font_size(int(grid_size))
            button.draw()

    def draw_success_message(self, grid_size):
        if self.sudoku.solved:
            font = pygame.font.SysFont("comicsans", int(grid_size))
            text = font.render("Congratulations!", 1, (0, 0, 0))
            self.canvas.screen.blit(text, (0, grid_size * 10))

    def draw_exit_button(self, x_size):
        self.exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self.exit_button.draw()
