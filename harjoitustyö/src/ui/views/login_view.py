from ui.view import View
from ui.components.button import Button
from ui.components.textbox import Textbox
from ui.components.form import Form
from ui.components.text import text


class LoginView(View):
    def __init__(self, canvas: "Canvas", login):
        self.canvas = canvas
        self.login = login

        self.exit_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "X", ((0, 0, 0), 3), login.open_menu
        )

        self.to_register_button = Button(
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

        self.login_form = Form(login.validate)

        self.username_textbox = Textbox(
            canvas,
            self.login_form,
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
            self.set_username,
        )

        self.password_textbox = Textbox(
            canvas,
            self.login_form,
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
            self.set_password,
        )

        self.login_form.attach_textbox(self.username_textbox)
        self.login_form.attach_textbox(self.password_textbox)

        self.login_button = Button(
            canvas,
            (0, 255, 0),
            0,
            300,
            100,
            50,
            "Login",
            ((0, 0, 0), 3),
            login.login,
        )

    def set_username(self, username):
        self.login.username = username

    def set_password(self, password):
        self.login.password = password

    def tick(self):
        self.draw()

    def draw(self):
        x_size, y_size = self.canvas.screen_dimensions

        # Draw login form
        text(
            self.canvas,
            "Login",
            x_size / 2 - self.username_textbox.width / 2,
            y_size * 0.075,
            (0, 0, 0),
            self.canvas.font_size,
        )

        self.username_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.username_textbox.update_position(
            x_size / 2 - self.username_textbox.width / 2, y_size * 0.15
        )
        self.username_textbox.draw()

        self.password_textbox.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.password_textbox.update_position(
            x_size / 2 - self.password_textbox.width / 2, y_size * 0.3
        )
        self.password_textbox.draw()

        self.login_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.login_button.update_position(
            x_size / 2 - self.login_button.width / 2, y_size * 0.45
        )
        self.login_button.draw()

        self.to_register_button.update_size(
            self.canvas.lower_screen_dimension * 0.4,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.to_register_button.update_position(
            x_size / 2 - self.to_register_button.width / 2, y_size * 0.6
        )
        self.to_register_button.draw()

        # Draw exit button
        self.exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self.exit_button.draw()
