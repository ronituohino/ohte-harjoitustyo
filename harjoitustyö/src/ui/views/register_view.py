from ui.view import View
from ui.components.button import Button
from ui.components.textbox import Textbox
from ui.components.form import Form
from ui.components.text import text


class RegisterView(View):
    """Luokka rekisteröitymisnäkymälle

    Attributes:
        canvas: Canvas -luokan referenssi
        register: Register -luokan referenssi
    """

    def __init__(self, canvas: "Canvas", register):
        """Luokan konstruktori

        Args:
            canvas: Canvas -luokan referenssi
            register: Register -luokan referenssi
        """

        self.canvas = canvas
        self.register = register

        self._exit_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "X", ((0, 0, 0), 3), register.open_menu
        )

        self._to_login_button = Button(
            canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "Already have an account?",
            ((0, 0, 0), 3),
            register.open_login,
        )

        self._register_form = Form(register.validate)

        self._username_textbox = Textbox(
            canvas,
            self._register_form,
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
            self._register_form,
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

        self._password_again_textbox = Textbox(
            canvas,
            self._register_form,
            "password_again",
            (245, 245, 245),
            0,
            400,
            200,
            50,
            None,
            "Password again",
            (200, 200, 200),
            ((0, 0, 0), 3),
            self._set_password_again,
        )

        self._register_form.attach_textbox(self._username_textbox)
        self._register_form.attach_textbox(self._password_textbox)
        self._register_form.attach_textbox(self._password_again_textbox)

        self.register_button = Button(
            canvas,
            (0, 255, 0),
            0,
            600,
            100,
            50,
            "Register",
            ((0, 0, 0), 3),
            register.register,
        )

    def _set_username(self, username):
        self.register.username = username

    def _set_password(self, password):
        self.register.password = password

    def _set_password_again(self, password_again):
        self.register.password_again = password_again

    def tick(self):
        """Päivittää rekisteröitymisnäkymän"""

        self.draw()

    def draw(self):
        """Piirtää rekisteröitymisnäkymän ikkunaan"""

        x_size, y_size = self.canvas.screen_dimensions

        # Draw registration form
        text(
            self.canvas,
            "Register",
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

        self._password_again_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._password_again_textbox.update_position(
            x_size / 2 - self._password_again_textbox.width / 2, y_size * 0.45
        )
        self._password_again_textbox.draw()

        self.register_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.register_button.update_position(
            x_size / 2 - self.register_button.width / 2, y_size * 0.6
        )
        self.register_button.draw()

        self._to_login_button.update_size(
            self.canvas.lower_screen_dimension * 0.7,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._to_login_button.update_position(
            x_size / 2 - self._to_login_button.width / 2, y_size * 0.75
        )
        self._to_login_button.draw()

        # Draw exit button
        self._exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self._exit_button.draw()
