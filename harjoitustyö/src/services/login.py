class Login:
    def __init__(self, game):
        self.game = game
        self.username = None
        self.password = None

    def __name__(self):
        return "Login"

    def username_validation(self, username):
        errors = []

        if not username:
            errors.append("Username is required")
        if not username or len(username) < 2:
            errors.append("Username must be at least 2 characters long")

        return errors

    def password_validation(self, password):
        errors = []

        if not password:
            errors.append("Password is required")
        if not password or len(password) < 4:
            errors.append("Password must be at least 4 characters long")

        return errors

    def login(self):
        errors = {}
        err = self.username_validation(self.username)
        if len(err) > 0:
            errors["username"] = err
        err = self.password_validation(self.password)
        if len(err) > 0:
            errors["password"] = err

        if len(errors.keys()) > 0:
            print(errors)
            return errors

        print("success")
        return True

    def open_menu(self):
        self.game.open_menu()
