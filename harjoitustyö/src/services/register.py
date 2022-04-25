from utils.validation import (
    username_validation,
    password_validation,
    password_again_validation,
)


class Register:
    def __init__(self, game):
        self.game = game
        self.username = None
        self.password = None
        self.password_again = None

    def __name__(self):
        return "Register"

    def validate(self):
        errors = {}
        err = username_validation(self.username)
        if len(err) > 0:
            errors["username"] = err
        err = password_validation(self.password)
        if len(err) > 0:
            errors["password"] = err
        err = password_again_validation(self.password, self.password_again)
        if len(err) > 0:
            errors["password_again"] = err
        return errors

    def register(self):
        errors = self.validate()

        if len(errors.keys()) > 0:
            print(errors)
            return errors

        result = self.game.database.create_account(self.username, self.password)
        if not result:
            return {"register": "Username already taken"}
        else:
            self.game.user = result
            self.game.open_menu()

    def open_menu(self):
        self.game.open_menu()

    def open_login(self):
        self.game.open_login()
