import pygame
from ui.view import View
from ui.components.button import Button
from ui.components.text import render, blit, text
from ui.components.box import box_outlined


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

        self._init_move_buttons()
        self._init_open_button()
        self._init_login_button()
        self._init_logout_button()

    def _init_move_buttons(self):
        self._move_buttons = [
            self._init_left_move_button(),
            self._init_right_move_button(),
        ]

    def _init_left_move_button(self):
        return Button(
            self.canvas,
            (255, 0, 0),
            0,
            self.canvas.screen_dimensions[1] / 2,
            100,
            50,
            "<-",
            ((0, 0, 0), 3),
            self.menu.move_left,
        )

    def _init_right_move_button(self):
        return Button(
            self.canvas,
            (255, 0, 0),
            400,
            self.canvas.screen_dimensions[1] / 2,
            100,
            50,
            "->",
            ((0, 0, 0), 3),
            self.menu.move_right,
        )

    def _init_open_button(self):
        self._open_button = Button(
            self.canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "Play",
            ((0, 0, 0), 3),
            self.menu.open_sudoku,
        )

    def _init_login_button(self):
        self._login_button = Button(
            self.canvas,
            (0, 0, 255),
            0,
            0,
            100,
            50,
            "Login",
            ((0, 0, 0), 3),
            self.menu.open_login,
        )

    def _init_logout_button(self):
        self._logout_button = Button(
            self.canvas,
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

        self._draw_choose_sudoku_text(x_size, y_size)

        self._draw_sudokus(x_size, y_size)

        self._draw_move_buttons(x_size, y_size)
        self._draw_open_sudoku_button(x_size, y_size)

        # Draw top bar
        if not self.menu.game.user:
            self._draw_login_button(x_size)
        else:
            self._draw_logout_button(x_size)
            self._draw_username()

    def _draw_choose_sudoku_text(self, x_size, y_size):
        ren = render(
            "Choose sudoku",
            (0, 0, 0),
            self.canvas.font_size,
        )
        blit(self.canvas, x_size * 0.5 - ren.get_size()[0] / 2, y_size * 0.3, ren)

    def _draw_sudokus(self, x_size, y_size):
        for i in range(-1, 2):
            rendered_sudoku = self.menu.selected_sudoku + i
            if rendered_sudoku >= 0 and rendered_sudoku < self.menu.sudoku_amount:
                # Render name text, but don't draw yet
                sudoku_name = self.menu.sudokus[rendered_sudoku]
                ren = self._render_sudoku_name(sudoku_name)
                x_center = x_size * 0.5 + x_size * 0.33 * (i)
                name_x_pos = x_center - ren.get_size()[0] / 2
                name_y_pos = y_size * 0.5 - ren.get_size()[1] / 2

                self._draw_sudokus_name_box(ren, name_x_pos, name_y_pos)

                # Completetion marks
                completion_times = [
                    t[1] for t in self.menu.completed_data if t[0] == sudoku_name
                ]
                if len(completion_times) > 0:
                    self._draw_sudokus_completed_mark(x_center, y_size)
                    self._draw_sudokus_time_mark(completion_times, x_center, y_size)

    def _render_sudoku_name(self, sudoku_name):
        return render(
            sudoku_name,
            (0, 0, 0),
            self.canvas.font_size,
        )

    def _draw_sudokus_name_box(self, ren, name_x_pos, name_y_pos):
        # Render outline
        box_outlined(
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

    def _draw_sudokus_completed_mark(self, x_center, y_size):
        ren = render(
            "Completed",
            (0, 0, 0),
            self.canvas.font_size,
        )
        box_outlined(
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

    def _draw_sudokus_time_mark(self, completion_times, x_center, y_size):
        time_str = "{:.2f}".format(min(completion_times))
        ren = self._render_sudokus_time_mark(time_str)
        box_outlined(
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

    def _render_sudokus_time_mark(self, time_str):
        return render(
            f"Time: {time_str}",
            (255, 255, 255),
            self.canvas.font_size,
        )

    def _draw_move_buttons(self, x_size, y_size):
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

    def _draw_open_sudoku_button(self, x_size, y_size):
        self._open_button.update_size(
            self.canvas.lower_screen_dimension * 0.2,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._open_button.update_position(
            x_size / 2 - self.canvas.lower_screen_dimension * 0.1,
            y_size - self.canvas.lower_screen_dimension * 0.1,
        )
        self._open_button.draw()

    def _draw_login_button(self, x_size):
        self._login_button.update_size(
            self.canvas.lower_screen_dimension * 0.2,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._login_button.update_position(
            x_size / 2 - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self._login_button.draw()

    def _draw_logout_button(self, x_size):
        self._logout_button.update_size(
            self.canvas.lower_screen_dimension * 0.2,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._logout_button.update_position(
            x_size / 2 - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self._logout_button.draw()

    def _draw_username(self):
        ren = render(
            f"Logged in: {self.menu.game.user['username']}",
            (0, 0, 0),
            self.canvas.font_size,
        )

        blit(
            self.canvas,
            self._logout_button.x + self._logout_button.width + 15,
            self.canvas.lower_screen_dimension * 0.05 - ren.get_size()[1] / 2,
            ren,
        )
