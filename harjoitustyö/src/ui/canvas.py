from ui.views.menu_view import MenuView
from ui.views.sudoku_view import SudokuView
from ui.views.login_view import LoginView
from ui.views.register_view import RegisterView

from utils.resolution import get_lower_res, get_font_size

# Game canvas, handles UI elements


class Canvas:
    def __init__(self, screen, screen_dimensions):
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.buttons = []

        self.lower_screen_dimension = get_lower_res(self.screen_dimensions)
        self.font_size = get_font_size(self.lower_screen_dimension)

        self.service_view = None

    def set_service(self, service):
        # Service has changed, update view
        # First remove old view's ui elements (buttons)
        self.buttons = []
        name = service.__name__()
        if name == "Menu":
            self.service_view = MenuView(self, service)
        elif name == "Sudoku":
            self.service_view = SudokuView(self, service)
        elif name == "Login":
            self.service_view = LoginView(self, service)
        elif name == "Register":
            self.service_view = RegisterView(self, service)

    def tick(self):
        self.service_view.tick()

    def add_button(self, button: "Button"):
        self.buttons.append(button)

    def remove_button(self, button: "Button"):
        self.buttons.remove(button)

    def handle_click(self, event: "Event"):
        if event.button == 1:  # Left click
            for button in self.buttons:
                if button.is_over(event.pos):
                    button.click()

    def update_screen_dimensions(self, event):
        self.screen_dimensions[0] = event.w
        self.screen_dimensions[1] = event.h

        self.lower_screen_dimension = get_lower_res(self.screen_dimensions)
        self.font_size = get_font_size(self.lower_screen_dimension)
