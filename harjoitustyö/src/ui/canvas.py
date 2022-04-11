from ui.views.menu_view import MenuView
from ui.views.sudoku_view import SudokuView

# Game canvas, handles UI elements


class Canvas:
    def __init__(self, screen, screen_dimensions):
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.buttons = []

        menu_view = MenuView(self)
        self.current_view = menu_view

    def tick(self, screen_dimensions):
        self.screen_dimensions = screen_dimensions
        self.current_view.tick(self.screen, screen_dimensions)

    def add_button(self, button: "Button"):
        self.buttons.append(button)

    def remove_button(self, button: "Button"):
        self.buttons.remove(button)

    def handle_click(self, event: "Event"):
        if event.button == 1:  # Left click
            for button in self.buttons:
                if button.is_over(event.pos):
                    button.click()
