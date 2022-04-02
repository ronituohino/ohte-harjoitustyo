# Game canvas, handles UI elements
class Canvas:
    def __init__(self):
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def remove_button(self, button):
        self.buttons.remove(button)

    def handle_click(self, event):
        if event.button == 1:  # Left click
            for button in self.buttons:
                if button.is_over(event.pos):
                    button.click()
