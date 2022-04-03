# Game canvas, handles UI elements

class Canvas:
    def __init__(self):
        self.buttons = []

    def add_button(self, button: "Button"):
        self.buttons.append(button)

    def remove_button(self, button: "Button"):
        self.buttons.remove(button)

    def handle_click(self, event: "Event"):
        if event.button == 1:  # Left click
            for button in self.buttons:
                if button.is_over(event.pos):
                    button.click()
