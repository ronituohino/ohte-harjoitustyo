from ui.view import View
from ui.button import Button


class LoginView(View):
    def __init__(self, canvas: "Canvas", login):
        self.canvas = canvas
        self.login = login

        self.exit_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "back", 20, None, login.open_menu
        )

        self.login_button = Button(
            canvas, (0, 255, 0), 0, 0, 100, 50, "login", 20, None, None
        )

        self.register_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "new user?", 20, None, None
        )

    def tick(self):
        self.draw()

    def draw(self):
        x_size, y_size = self.canvas.screen_dimensions

        # Draw exit button
        self.exit_button.update_size(
            self.canvas.lower_screen_dimension * 0.1,
            self.canvas.lower_screen_dimension * 0.1,
        )
        self.exit_button.update_position(
            x_size - self.canvas.lower_screen_dimension * 0.1, 0
        )
        self.exit_button.draw()
