from ui.view import View
from ui.components.button import Button
from ui.components.textbox import Textbox
from ui.components.form import Form
from ui.components.text import text


class LoginView(View):
    """Luokka kirjautumisnäkymälle

    Attributes:
        canvas: Canvas -luokan referenssi
        login: Login -luokan referenssi
    """

    def __init__(self, canvas: "Canvas", login):
        """Luokan konstruktori

        Args:
            canvas: Canvas -luokan referenssi
            login: Login -luokan referenssi
        """

        self.canvas = canvas
        self.login = login

        self._exit_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "X", ((0, 0, 0), 3), login.open_menu
        )

        self._to_register_button = Button(
            canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "New user?",
            ((0, 0, 0), 3),
            login.open_register,
        )

        self._login_form = Form(login.validate)

        self._username_textbox = Textbox(
            canvas,
            self._login_form,
            "username",
            (245, 245, 245),
            0,
            0,
            200,
            50,
            14,
            "Username",
            (200, 200, 200),
            ((0, 0, 0), 3),
            self._set_username,
        )

        self._password_textbox = Textbox(
            canvas,
            self._login_form,
            "password",
            (245, 245, 245),
            0,
            200,
            200,
            50,
            None,
            "Password",
            (200, 200, 200),
            ((0, 0, 0), 3),
            self._set_password,
        )

        self._login_form.attach_textbox(self._username_textbox)
        self._login_form.attach_textbox(self._password_textbox)

        self._login_button = Button(
            canvas,
            (0, 255, 0),
            0,
            300,
            100,
            50,
            "Login",
            ((0, 0, 0), 3),
            self._attempt_login,
        )

    def _attempt_login(self):
        return self.login.login()

    def _set_username(self, username):
        self.login.username = username

    def _set_password(self, password):
        self.login.password = password

    def tick(self):
        """Päivittää kirjautumisnäkymän"""

        self.draw()

    def draw(self):
        """Piirtää kirjautumisnäkymän ikkunaan"""

        x_size, y_size = self.canvas.screen_dimensions

        # Draw login form
        text(
            self.canvas,
            "Login",
            x_size / 2 - self._username_textbox.width / 2,
            y_size * 0.075,
            (0, 0, 0),
            self.canvas.font_size,
        )

        self._username_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._username_textbox.update_position(
            x_size / 2 - self._username_textbox.width / 2, y_size * 0.15
        )
        self._username_textbox.draw()

        self._password_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._password_textbox.update_position(
            x_size / 2 - self._password_textbox.width / 2, y_size * 0.3
        )
        self._password_textbox.draw()

        if self._login_button.return_val != None:
            text(
                self.canvas,
                self._login_button.return_val["login"],
                x_size / 2 - self._password_textbox.width / 2,
                y_size * 0.45,
                (200, 0, 0),
                self.canvas.font_size * 0.5,
            )

        self._login_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._login_button.update_position(
            x_size / 2 - self._login_button.width / 2, y_size * 0.5
        )
        self._login_button.draw()

        self._to_register_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._to_register_button.update_position(
            x_size / 2 - self._to_register_button.width / 2, y_size * 0.65
        )
        self._to_register_button.draw()

        # Draw exit button
        self._exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self._exit_button.draw()
