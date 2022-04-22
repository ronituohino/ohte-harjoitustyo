from ui.view import View
from ui.components.button import Button
from ui.components.textbox import Textbox


class LoginView(View):
    def __init__(self, canvas: "Canvas", login):
        self.canvas = canvas
        self.login = login

        self.exit_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "back", 20, None, login.open_menu
        )

        self.register_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "new user?", 20, None, None
        )

        self.username_textbox = Textbox(
            canvas,
            (245, 245, 245),
            0,
            0,
            200,
            50,
            "Username",
            (200, 200, 200),
            30,
            ((0, 0, 0), 3),
            login.username_validation,
            self.set_username,
        )

        self.password_textbox = Textbox(
            canvas,
            (245, 245, 245),
            0,
            200,
            200,
            50,
            "Password",
            (200, 200, 200),
            30,
            ((0, 0, 0), 3),
            login.password_validation,
            self.set_password,
        )

        self.login_button = Button(
            canvas, (0, 255, 0), 0, 300, 100, 50, "login", 20, None, login.login
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
        self.username_textbox.draw()
        self.password_textbox.draw()
        self.login_button.draw()

        # Draw exit button
        self.exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self.exit_button.draw()
