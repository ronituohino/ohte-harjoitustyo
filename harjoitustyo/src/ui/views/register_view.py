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

        self._init_exit_button()
        self._init_to_login_button()
        self._register_form = Form(register.validate)
        self._init_username_textbox()
        self._init_password_textbox()
        self._init_password_again_textbox()
        self._register_form.attach_textbox(self._username_textbox)
        self._register_form.attach_textbox(self._password_textbox)
        self._register_form.attach_textbox(self._password_again_textbox)
        self._init_register_button()

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
            self.register.open_menu,
        )

    def _init_to_login_button(self):
        self._to_login_button = Button(
            self.canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "Already have an account?",
            ((0, 0, 0), 3),
            self.register.open_login,
        )

    def _init_username_textbox(self):
        self._username_textbox = Textbox(
            self.canvas,
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

    def _init_password_textbox(self):
        self._password_textbox = Textbox(
            self.canvas,
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

    def _init_password_again_textbox(self):
        self._password_again_textbox = Textbox(
            self.canvas,
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

    def _init_register_button(self):
        self._register_button = Button(
            self.canvas,
            (0, 255, 0),
            0,
            600,
            100,
            50,
            "Register",
            ((0, 0, 0), 3),
            self._attempt_register,
        )

    def _attempt_register(self):
        self._register_form.validate()
        return self.register.register()

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

        self._draw_register_text(x_size, y_size)

        self._draw_username_textbox(x_size, y_size)
        self._draw_password_textbox(x_size, y_size)
        self._draw_password_again_textbox(x_size, y_size)
        self._draw_registration_error(x_size, y_size)
        self._draw_register_button(x_size, y_size)
        self._draw_to_login_button(x_size, y_size)

        self._draw_exit_button(x_size)

    def _draw_register_text(self, x_size, y_size):
        text(
            self.canvas,
            "Register",
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

    def _draw_password_again_textbox(self, x_size, y_size):
        self._password_again_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._password_again_textbox.update_position(
            x_size / 2 - self._password_again_textbox.width / 2, y_size * 0.45
        )
        self._password_again_textbox.draw()

    def _draw_registration_error(self, x_size, y_size):
        if (
            self._register_button.return_val != None
            and "register" in self._register_button.return_val
        ):
            text(
                self.canvas,
                self._register_button.return_val["register"],
                x_size / 2 - self._password_textbox.width / 2,
                y_size * 0.6,
                (200, 0, 0),
                self.canvas.font_size * 0.5,
            )

    def _draw_register_button(self, x_size, y_size):
        self._register_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._register_button.update_position(
            x_size / 2 - self._register_button.width / 2, y_size * 0.65
        )
        self._register_button.draw()

    def _draw_to_login_button(self, x_size, y_size):
        self._to_login_button.update_size(
            self.canvas.lower_screen_dimension * 0.7,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._to_login_button.update_position(
            x_size / 2 - self._to_login_button.width / 2, y_size * 0.8
        )
        self._to_login_button.draw()

    def _draw_exit_button(self, x_size):
        self._exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self._exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self._exit_button.draw()
