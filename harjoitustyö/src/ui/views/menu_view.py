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
                "<-",
                ((0, 0, 0), 3),
                self.menu.move_left,
            ),
            Button(
                canvas,
                (255, 0, 0),
                400,
                canvas.screen_dimensions[1] / 2,
                100,
                50,
                "->",
                ((0, 0, 0), 3),
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
            "Play",
            ((0, 0, 0), 3),
            self.menu.open_sudoku,
        )

        self.login_button = Button(
            canvas,
            (0, 0, 255),
            0,
            0,
            100,
            50,
            "Login",
            ((0, 0, 0), 3),
            self.menu.open_login,
        )
        self.logout_button = Button(
            canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "Logout",
            ((0, 0, 0), 3),
            self.menu.logout,
        )

    def tick(self):
        self.draw()

    def draw(self):
        x_size, y_size = self.canvas.screen_dimensions

        # Draw selectable sudokus
        for i in range(-1, 2):
            rendered_sudoku = self.menu.selected_sudoku + i
            if rendered_sudoku >= 0 and rendered_sudoku < self.menu.sudoku_amount:
                # Render name text, but don't draw yet
                sudoku_name = self.menu.sudokus[rendered_sudoku].replace(".sudoku", "")
                ren = render(
                    sudoku_name,
                    (0, 0, 0),
                    self.canvas.font_size,
                )
                name_x_pos = x_size * 0.5 + x_size * 0.33 * (i) - ren.get_size()[0] / 2
                name_y_pos = y_size * 0.35 - ren.get_size()[1] / 2

                # Render outline
                pygame.draw.rect(
                    self.canvas.screen,
                    (0, 0, 0),
                    (
                        name_x_pos - 8,
                        name_y_pos - 8,
                        ren.get_size()[0] + 8 + 11,
                        ren.get_size()[1] + 8 + 11,
                    ),
                )

                pygame.draw.rect(
                    self.canvas.screen,
                    (255, 255, 255),
                    (
                        name_x_pos - 5,
                        name_y_pos - 5,
                        ren.get_size()[0] + 8 + 5,
                        ren.get_size()[1] + 8 + 5,
                    ),
                )

                # Draw name on top of outline stuff
                blit(
                    self.canvas,
                    name_x_pos,
                    name_y_pos,
                    ren,
                )

                # Completed mark
                print(sudoku_name)
                print(self.menu.completed_sudokus)
                if sudoku_name in self.menu.completed_sudokus:
                    text(
                        self.canvas,
                        "Completed",
                        name_x_pos,
                        y_size * 0.5,
                        (0, 255, 0),
                        self.canvas.font_size,
                    )

        # Draw left/right buttons
        for i in range(2):
            button = self.move_buttons[i]
            button.update_size(
                self.canvas.lower_screen_dimension * 0.2,
                self.canvas.lower_screen_dimension * 0.1,
            )
            if i == 0:
                button.update_position(
                    x_size * 0.1,
                    y_size * 0.65 - self.canvas.lower_screen_dimension * 0.05,
                )
            if i == 1:
                button.update_position(
                    x_size - self.canvas.lower_screen_dimension * 0.2 - x_size * 0.1,
                    y_size * 0.65 - self.canvas.lower_screen_dimension * 0.05,
                )
            button.draw()

        # Draw open Sudoku button
        self.open_button.update_size(
            self.canvas.lower_screen_dimension * 0.2,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.open_button.update_position(
            x_size / 2 - self.canvas.lower_screen_dimension * 0.1,
            y_size * 0.65 - self.canvas.lower_screen_dimension * 0.05,
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
            ren = render(
                f"Logged in: {self.menu.game.user['username']}",
                (0, 0, 0),
                self.canvas.font_size,
            )

            blit(
                self.canvas,
                self.logout_button.x + self.logout_button.width + 15,
                self.canvas.lower_screen_dimension * 0.05 - ren.get_size()[1] / 2,
                ren,
            )
