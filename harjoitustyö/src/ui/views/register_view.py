from ui.view import View


class RegisterView(View):
    def __init__(self, canvas: "Canvas", register):
        self.canvas = canvas
        self.register = register

        self.exit_button = Button(
            canvas, (255, 0, 0), 0, 0, 100, 50, "back", 20, None, register.open_menu
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
