import os
from os.path import isfile, join
import pygame
from ui.view import View
from ui.components.button import Button
from ui.components.text import render, blit, text
from ui.components.box import box
from services.menu import Menu


class MenuView(View):
    """Luokka päävalikkonäkymälle

    Attributes:
        canvas: Canvas -luokan referenssi
        menu: Menu -luokan referenssi
    """

    def __init__(self, canvas: "Canvas", menu):
        """Luokan konstruktori

        Args:
            canvas: Canvas -luokan referenssi
            menu: Menu -luokan referenssi
        """

        self.canvas = canvas
        self.menu = menu

        # UI
        self._move_buttons = [
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

        self._open_button = Button(
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

        self._login_button = Button(
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
        self._logout_button = Button(
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
        """Päivittää päävalikkonäkymän"""

        self.draw()

    def draw(self):
        """Piirtää päävalikkonäkymän ikkunaan"""

        x_size, y_size = self.canvas.screen_dimensions

        ren = render(
            "Choose sudoku",
            (0, 0, 0),
            self.canvas.font_size,
        )
        blit(self.canvas, x_size * 0.5 -
             ren.get_size()[0] / 2, y_size * 0.3, ren)

        # Draw selectable sudokus
        for i in range(-1, 2):
            rendered_sudoku = self.menu.selected_sudoku + i
            if rendered_sudoku >= 0 and rendered_sudoku < self.menu.sudoku_amount:
                # Render name text, but don't draw yet
                sudoku_name = self.menu.sudokus[rendered_sudoku]
                ren = render(
                    sudoku_name,
                    (0, 0, 0),
                    self.canvas.font_size,
                )
                x_center = x_size * 0.5 + x_size * 0.33 * (i)
                name_x_pos = x_center - ren.get_size()[0] / 2
                name_y_pos = y_size * 0.5 - ren.get_size()[1] / 2

                # Render outline
                box(
                    self.canvas,
                    (255, 255, 255),
                    name_x_pos,
                    name_y_pos,
                    ren.get_size()[0],
                    ren.get_size()[1],
                    ((0, 0, 0), 3, 5),
                )

                # Draw name on top of outline stuff
                blit(
                    self.canvas,
                    name_x_pos,
                    name_y_pos,
                    ren,
                )

                # Completetion stuff
                completion_times = [
                    t[1] for t in self.menu.completed_data if t[0] == sudoku_name
                ]
                if len(completion_times) > 0:
                    # 'Completed' mark
                    ren = render(
                        "Completed",
                        (0, 0, 0),
                        self.canvas.font_size,
                    )
                    box(
                        self.canvas,
                        (0, 255, 0),
                        x_center - ren.get_size()[0] / 2,
                        y_size * 0.6 - ren.get_size()[1] / 2,
                        ren.get_size()[0],
                        ren.get_size()[1],
                        ((0, 0, 0), 3, 3),
                    )
                    blit(
                        self.canvas,
                        x_center - ren.get_size()[0] / 2,
                        y_size * 0.6 - ren.get_size()[1] / 2,
                        ren,
                    )

                    # Time
                    time_str = "{:.2f}".format(min(completion_times))
                    ren = render(
                        f"Time: {time_str}",
                        (255, 255, 255),
                        self.canvas.font_size,
                    )
                    box(
                        self.canvas,
                        (0, 0, 255),
                        x_center - ren.get_size()[0] / 2,
                        y_size * 0.7 - ren.get_size()[1] / 2,
                        ren.get_size()[0],
                        ren.get_size()[1],
                        ((0, 0, 0), 3, 3),
                    )
                    blit(
                        self.canvas,
                        x_center - ren.get_size()[0] / 2,
                        y_size * 0.7 - ren.get_size()[1] / 2,
                        ren,
                    )

        # Draw left/right buttons
        for i in range(2):
            button = self._move_buttons[i]
            button.update_size(
                self.canvas.lower_screen_dimension * 0.2,
                self.canvas.lower_screen_dimension * 0.1,
            )
            if i == 0:
                button.update_position(
                    x_size * 0.1,
                    y_size - self.canvas.lower_screen_dimension * 0.1,
                )
            if i == 1:
                button.update_position(
                    x_size - self.canvas.lower_screen_dimension * 0.2 - x_size * 0.1,
                    y_size - self.canvas.lower_screen_dimension * 0.1,
                )
            button.draw()

        # Draw open Sudoku button
        self._open_button.update_size(
            self.canvas.lower_screen_dimension * 0.2,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._open_button.update_position(
            x_size / 2 - self.canvas.lower_screen_dimension * 0.1,
            y_size - self.canvas.lower_screen_dimension * 0.1,
        )
        self._open_button.draw()

        # Draw login / logout button
        if not self.menu.game.user:
            self._login_button.update_size(
                self.canvas.lower_screen_dimension * 0.2,
                self.canvas.lower_screen_dimension * 0.1,
            )
            self._login_button.update_position(
                x_size / 2 - self.canvas.lower_screen_dimension * 0.1, 0
            )
            self._login_button.draw()
        else:
            # Logout button
            self._logout_button.update_size(
                self.canvas.lower_screen_dimension * 0.2,
                self.canvas.lower_screen_dimension * 0.1,
            )
            self._logout_button.update_position(
                x_size / 2 - self.canvas.lower_screen_dimension * 0.1, 0
            )
            self._logout_button.draw()

            # Username
            ren = render(
                f"Logged in: {self.menu.game.user['username']}",
                (0, 0, 0),
                self.canvas.font_size,
            )

            blit(
                self.canvas,
                self._logout_button.x + self._logout_button.width + 15,
                self.canvas.lower_screen_dimension *
                0.05 - ren.get_size()[1] / 2,
                ren,
            )
