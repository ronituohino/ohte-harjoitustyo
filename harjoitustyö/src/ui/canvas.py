from views.menu import Menu

# Game canvas, handles UI elements


class Canvas:
    def __init__(self, screen, screen_dimensions):
        self.screen = screen
        self.buttons = []
        menu = Menu()
        menu.init_ui(self, screen_dimensions)
        self.current_view = menu

    def tick(self, screen_dimensions):
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
