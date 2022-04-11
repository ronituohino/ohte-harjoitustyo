import os
from os.path import isfile, join
import pygame
from ui.view import View
from ui.button import Button

from services.menu import Menu


class MenuView(View):
    def __init__(self, canvas: "Canvas"):
        self.menu = Menu()

        # UI
        self.move_buttons = [
            Button(
                canvas,
                (255, 0, 0),
                0,
                canvas.screen_dimensions[1] / 2,
                100,
                50,
                "left",
                20,
                None,
                self.menu.move_left,
            ),
            Button(
                canvas,
                (255, 0, 0),
                400,
                canvas.screen_dimensions[1] / 2,
                100,
                50,
                "right",
                20,
                None,
                self.menu.move_right,
            ),
        ]

    def tick(self, screen, screen_dimensions):
        self.draw(screen, screen_dimensions)

    def draw(self, screen, screen_dimensions):
        print(self.menu.selected_sudoku)
        font = pygame.font.SysFont("comicsans", 40)

        # Draw selectable sudokus
        for i in range(self.menu.selected_sudoku - 1, self.menu.selected_sudoku + 2):
            if i >= 0 and i < self.menu.sudoku_amount:
                text = font.render(self.menu.sudokus[i], 1, (0, 0, 0))
                screen.blit(text, (0, 100 * i))

        # Draw left/right buttons
        for button in self.move_buttons:
            button.draw(screen)
