from ui.views.menu_view import MenuView
from ui.views.sudoku_view import SudokuView

# Game canvas, handles UI elements


class Canvas:
    def __init__(self, screen, screen_dimensions):
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.buttons = []

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

    def update_screen_dimensions(event):
        self.screen_dimensions[0] = event.w
        self.screen_dimensions[1] = event.h
