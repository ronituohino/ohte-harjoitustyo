import os
from os.path import isfile, join
import pygame
from ui.view import View
from ui.button import Button


class Menu(View):
    def __init__(self):
        sudoku_path = f"{os.getcwd()}/sudokus"
        self.sudokus = [
            f for f in os.listdir(sudoku_path) if isfile(join(sudoku_path, f))
        ]
        self.selected_sudoku = 0
        self.sudoku_amount = len(self.sudokus)

        # UI
        self.move_buttons = None

    def init_ui(self, canvas: "Canvas", screen_dimensions: list):
        self.move_buttons = [
            Button(
                canvas,
                (255, 0, 0),
                0,
                screen_dimensions[1] / 2,
                100,
                50,
                "left",
                20,
                None,
                self.move_left,
            ),
            Button(
                canvas,
                (255, 0, 0),
                400,
                screen_dimensions[1] / 2,
                100,
                50,
                "right",
                20,
                None,
                self.move_right,
            ),
        ]

    def move_left(self):
        if self.selected_sudoku > 0:
            self.selected_sudoku -= 1

    def move_right(self):
        if self.selected_sudoku < self.sudoku_amount - 1:
            self.selected_sudoku += 1

    def tick(self, screen, screen_dimensions):
        self.draw(screen, screen_dimensions)

    def draw(self, screen, screen_dimensions):
        print(self.selected_sudoku)
        font = pygame.font.SysFont("comicsans", 40)

        # Draw selectable sudokus
        for i in range(self.selected_sudoku - 1, self.selected_sudoku + 2):
            if i >= 0 and i < self.sudoku_amount:
                text = font.render(self.sudokus[i], 1, (0, 0, 0))
                screen.blit(text, (0, 100 * i))

        # Draw left/right buttons
        for button in self.move_buttons:
            button.draw(screen)
