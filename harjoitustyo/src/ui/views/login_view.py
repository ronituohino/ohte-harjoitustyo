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

        self._init_exit_button()
        self._init_to_register_button()
        self._login_form = Form(login.validate)
        self._init_username_textbox()
        self._init_password_textbox()
        self._login_form.attach_textbox(self._username_textbox)
        self._login_form.attach_textbox(self._password_textbox)
        self._init_login_button()

    def _init_exit_button(self):
        self._exit_button = Button(
            self.canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "X",
            ((0, 0, 0), 3),
            self.login.open_menu,
        )

    def _init_to_register_button(self):
        self._to_register_button = Button(
            self.canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "New user?",
            ((0, 0, 0), 3),
            self.login.open_register,
        )

    def _init_username_textbox(self):
        self._username_textbox = Textbox(
            self.canvas,
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

    def _init_password_textbox(self):
        self._password_textbox = Textbox(
            self.canvas,
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

    def _init_login_button(self):
        self._login_button = Button(
            self.canvas,
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
        self._login_form.validate()
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

        self._draw_login_text(x_size, y_size)

        self._draw_username_textbox(x_size, y_size)
        self._draw_password_textbox(x_size, y_size)
        self._draw_login_error(x_size, y_size)
        self._draw_login_button(x_size, y_size)
        self._draw_to_register_button(x_size, y_size)

        self._draw_exit_button(x_size)

    def _draw_login_text(self, x_size, y_size):
        text(
            self.canvas,
            "Login",
            x_size / 2 - self._username_textbox.width / 2,
            y_size * 0.075,
            (0, 0, 0),
            self.canvas.font_size,
        )

    def _draw_username_textbox(self, x_size, y_size):
        self._username_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._username_textbox.update_position(
            x_size / 2 - self._username_textbox.width / 2, y_size * 0.15
        )
        self._username_textbox.draw()

    def _draw_password_textbox(self, x_size, y_size):
        self._password_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._password_textbox.update_position(
            x_size / 2 - self._password_textbox.width / 2, y_size * 0.3
        )
        self._password_textbox.draw()

    def _draw_login_error(self, x_size, y_size):
        if (
            self._login_button.return_val != None
            and "login" in self._login_button.return_val
        ):
            text(
                self.canvas,
                self._login_button.return_val["login"],
                x_size / 2 - self._password_textbox.width / 2,
                y_size * 0.45,
                (200, 0, 0),
                self.canvas.font_size * 0.5,
            )

    def _draw_login_button(self, x_size, y_size):
        self._login_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._login_button.update_position(
            x_size / 2 - self._login_button.width / 2, y_size * 0.5
        )
        self._login_button.draw()

    def _draw_to_register_button(self, x_size, y_size):
        self._to_register_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._to_register_button.update_position(
            x_size / 2 - self._to_register_button.width / 2, y_size * 0.65
        )
        self._to_register_button.draw()

    def _draw_exit_button(self, x_size):
        self._exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self._exit_button.draw()
