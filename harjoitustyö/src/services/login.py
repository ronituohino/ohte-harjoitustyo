from utils.validation import username_validation, password_validation


class Login:
    def __init__(self, game):
        self.game = game
        self.username = None
        self.password = None

    def __name__(self):
        return "Login"

    def validate(self):
        errors = {}
        err = username_validation(self.username)
        if len(err) > 0:
            errors["username"] = err
        err = password_validation(self.password)
        if len(err) > 0:
            errors["password"] = err
        return errors

    def login(self):
        errors = self.validate()

        if len(errors.keys()) > 0:
            print(errors)
            return errors

        result = self.game.database.login(self.username, self.password)
        if not result:
            return {"login": "Username or password invalid"}
        else:
            self.game.user = result
            self.game.open_menu()

    def open_menu(self):
        self.game.open_menu()

    def open_register(self):
        self.game.open_register()
