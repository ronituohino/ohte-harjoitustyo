import os
from os.path import isfile, join
import pygame
from ui.view import View
from ui.components.button import Button
from ui.components.text import render, blit, text
from services.menu import Menu


class MenuView(View):
    def __init__(self, canvas: "Canvas", menu):
        self.canvas = canvas
        self.menu = menu

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
                None,
                self.menu.move_right,
            ),
        ]

        self.open_button = Button(
            canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "open",
            None,
            self.menu.open_sudoku,
        )

        self.login_button = Button(
            canvas, (0, 0, 255), 0, 0, 100, 50, "login", None, self.menu.open_login
        )
        self.logout_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "logout", None, self.menu.logout
        )

    def tick(self):
        self.draw()

    def draw(self):
        x_size, y_size = self.canvas.screen_dimensions

        # Draw selectable sudokus
        for i in range(-1, 2):
            rendered_sudoku = self.menu.selected_sudoku + i
            if rendered_sudoku >= 0 and rendered_sudoku < self.menu.sudoku_amount:
                ren = render(
                    self.menu.sudokus[rendered_sudoku], (
                        0, 0, 0), self.canvas.font_size
                )
                blit(
                    self.canvas,
                    x_size * 0.5 + x_size * 0.33 * (i) - ren.get_size()[0] / 2,
                    y_size * 0.2,
                    ren,
                )

        # Draw left/right buttons
        for i in range(2):
            button = self.move_buttons[i]
            button.update_size(
                self.canvas.lower_screen_dimension * 0.2,
                self.canvas.lower_screen_dimension * 0.1,
            )
            if i == 0:
                button.update_position(0, y_size / 2)
            if i == 1:
                button.update_position(
                    x_size - self.canvas.lower_screen_dimension * 0.2, y_size / 2
                )
            button.draw()

        # Draw open Sudoku button
        self.open_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.open_button.update_position(
            x_size / 2 - self.canvas.lower_screen_dimension * 0.05,
            y_size / 2 - self.canvas.lower_screen_dimension * 0.05,
        )
        self.open_button.draw()

        # Draw login / logout button
        if not self.menu.game.user:
            self.login_button.update_size(
                self.canvas.lower_screen_dimension * 0.2,
                self.canvas.lower_screen_dimension * 0.1,
            )
            self.login_button.update_position(
                x_size / 2 - self.canvas.lower_screen_dimension * 0.1, 0
            )
            self.login_button.draw()
        else:
            # Logout button
            self.logout_button.update_size(
                self.canvas.lower_screen_dimension * 0.2,
                self.canvas.lower_screen_dimension * 0.1,
            )
            self.logout_button.update_position(
                x_size / 2 - self.canvas.lower_screen_dimension * 0.1, 0
            )
            self.logout_button.draw()

            # Username
            text(
                self.canvas,
                f"logged in: {self.menu.game.user['username']}",
                self.logout_button.x + self.logout_button.width,
                0,
                (0, 0, 0),
                self.canvas.font_size,
            )
