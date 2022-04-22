class Register:
    def __init__(self, game):
        self.game = game

    def __name__(self):
        return "Register"

    def open_menu(self):
        self.game.open_menu()
