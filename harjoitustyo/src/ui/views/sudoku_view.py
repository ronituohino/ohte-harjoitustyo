import os
import pygame
from ui.components.button import Button
from ui.components.text import text
from ui.view import View
from services.sudoku import Sudoku

# Sudoku Game view


class SudokuView(View):
    """Luokka Sudoku -pelinäkymälle

    Attributes:
        canvas: Canvas -luokan referenssi
        sudoku: Sudoku -luokan referenssi
    """

    def __init__(self, canvas: "Canvas", sudoku) -> None:
        """Luokan konstruktori

        Args:
            canvas: Canvas -luokan referenssi
            sudoku: Sudoku -luokan referenssi
        """

        self.canvas = canvas
        self.sudoku = sudoku

        # Init UI elements
        self._sudoku_buttons = [None] * (9 * 9)
        x_size, y_size = canvas.screen_dimensions
        grid_size = self.canvas.lower_screen_dimension / 11
        for i in range(9):
            for j in range(9):
                self._sudoku_buttons[i * 9 + j] = Button(
                    canvas,
                    (100, 100, 100),
                    j * grid_size,
                    i * grid_size,
                    grid_size + 1,
                    grid_size + 1,
                    str(self.sudoku.grid[i * 9 + j]),
                    None,
                    self.sudoku.set_value,
                    (j, i),
                )

        self._number_buttons = [None] * 9
        for i in range(9):
            self._number_buttons[i] = Button(
                canvas,
                (100, 100, 100),
                10 * grid_size,
                i * grid_size,
                grid_size,
                grid_size,
                str(i + 1),
                ((0, 0, 0), 3),
                self.sudoku.set_selection_value,
                i + 1,
            )

        self._exit_button = Button(
            canvas,
            (255, 0, 0),
            x_size - self.canvas.lower_screen_dimension * 0.1,
            0,
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
            "exit",
            None,
            self.sudoku.exit_to_menu,
        )

    # Game UI functions
    # tick is called once per frame

    def tick(self) -> None:
        """Päivittää Sudoku -pelinäkymän"""

        self.draw()

    def draw(self) -> None:
        """Piirtää Sudoku -pelinäkymän ikkunaan"""

        x_size, y_size = self.canvas.screen_dimensions
        grid_size = self.canvas.lower_screen_dimension / 11

        self._draw_sudoku_buttons(grid_size)
        self._draw_sudoku_grid(grid_size)
        self._draw_number_selection(grid_size)
        self._draw_success_message(grid_size)
        self._draw_exit_button(x_size)

    def _draw_sudoku_buttons(self, grid_size):
        # Draw numbered squares
        for i in range(9):
            for j in range(9):
                value = self.sudoku.grid[i * 9 + j]
                button = self._sudoku_buttons[i * 9 + j]
                button.update_text(str(self.sudoku.grid[i * 9 + j]))
                button.update_position(j * grid_size, i * grid_size)
                button.update_size(grid_size + 1, grid_size + 1)
                if value > 0:
                    button.draw()

    def _draw_sudoku_grid(self, grid_size):
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

    def _draw_number_selection(self, grid_size):
        # Draw number selection buttons
        for i in range(9):
            button = self._number_buttons[i]
            button.update_position(10 * grid_size, i * grid_size)
            button.update_size(grid_size, grid_size)
            button.draw()

    def _draw_success_message(self, grid_size):
        if self.sudoku.solved:
            text(
                self.canvas,
                "Congratulations!",
                0,
                grid_size * 10,
                (0, 0, 0),
                self.canvas.font_size,
            )

    def _draw_exit_button(self, x_size):
        self._exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self._exit_button.draw()