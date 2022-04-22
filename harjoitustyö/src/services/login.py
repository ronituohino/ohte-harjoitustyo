class Login:
    def __init__(self, game):
        self.game = game

    def __name__(self):
        return "Login"

    def open_menu(self):
        self.game.open_menu()
