import unittest

from services.register import Register


class FakeDatabase:
    def create_account(self, username, password):
        return username != "username_taken"


class FakeGame:
    def __init__(self) -> None:
        self.user = None
        self.database = FakeDatabase()

        self.open_menu_called = 0
        self.open_login_called = 0

    def open_menu(self):
        self.open_menu_called += 1

    def open_login(self):
        self.open_login_called += 1


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.register = Register(FakeGame())

    def test_validate_correct(self):
        self.register.username = "roni"
        self.register.password = "12345"
        self.register.password_again = "12345"
        self.assertEqual(self.register.validate(), {})

    def test_validate_incorrect(self):
        self.register.username = "roni"
        self.register.password = "12345"
        self.register.password_again = "54321"
        self.assertEqual(
            self.register.validate(), {"password_again": [
                "Passwords have to match"]}
        )

    def test_open_menu(self):
        self.register.open_menu()
        self.assertEqual(self.register.game.open_menu_called, 1)

    def test_open_login(self):
        self.register.open_login()
        self.assertEqual(self.register.game.open_login_called, 1)

    def test_register_correct(self):
        self.register.username = "roni"
        self.register.password = "12345"
        self.register.password_again = "12345"
        self.register.register()
        self.assertEqual(self.register.game.user, True)

    def test_register_username_taken(self):
        self.register.username = "username_taken"
        self.register.password = "12345"
        self.register.password_again = "12345"
        self.assertEqual(
            self.register.register(), {"register": "Username already taken"}
        )
