from ui.view import View
from ui.components.button import Button
from ui.components.textbox import Textbox
from ui.components.form import Form


class RegisterView(View):
    def __init__(self, canvas: "Canvas", register):
        self.canvas = canvas
        self.register = register

        self.exit_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "back", 20, None, register.open_menu
        )

        self.login_button = Button(
            canvas,
            (255, 0, 0),
            0,
            0,
            100,
            50,
            "already have an account?",
            20,
            None,
            register.open_login,
        )

        self.register_form = Form(register.validate)

        self.username_textbox = Textbox(
            canvas,
            self.register_form,
            "username",
            (245, 245, 245),
            0,
            0,
            200,
            50,
            "Username",
            (200, 200, 200),
            30,
            ((0, 0, 0), 3),
            self.set_username,
        )

        self.password_textbox = Textbox(
            canvas,
            self.register_form,
            "password",
            (245, 245, 245),
            0,
            200,
            200,
            50,
            "Password",
            (200, 200, 200),
            30,
            ((0, 0, 0), 3),
            self.set_password,
        )

        self.password_again_textbox = Textbox(
            canvas,
            self.register_form,
            "password_again",
            (245, 245, 245),
            0,
            400,
            200,
            50,
            "Password again",
            (200, 200, 200),
            30,
            ((0, 0, 0), 3),
            self.set_password_again,
        )

        self.register_form.attach_textbox(self.username_textbox)
        self.register_form.attach_textbox(self.password_textbox)
        self.register_form.attach_textbox(self.password_again_textbox)

        self.register_button = Button(
            canvas, (0, 255, 0), 0, 600, 100, 50, "login", 20, None, register.register
        )

    def set_username(self, username):
        self.register.username = username

    def set_password(self, password):
        self.register.password = password

    def set_password_again(self, password_again):
        self.register.password_again = password_again

    def tick(self):
        self.draw()

    def draw(self):
        x_size, y_size = self.canvas.screen_dimensions

        # Draw registration form
        self.username_textbox.draw()
        self.password_textbox.draw()
        self.password_again_textbox.draw()
        self.register_button.draw()
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
