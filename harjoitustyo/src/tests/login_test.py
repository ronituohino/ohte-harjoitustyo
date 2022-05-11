import unittest

from services.login import Login


class FakeDatabase:
    def login(self, username, password):
        return username != "username_that_is_not_in_database"


class FakeGame:
    def __init__(self) -> None:
        self.user = None
        self.database = FakeDatabase()

        self.open_menu_called = 0
        self.open_register_called = 0

    def open_menu(self):
        self.open_menu_called += 1

    def open_register(self):
        self.open_register_called += 1


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = Login(FakeGame())

    def test_validate_correct(self):
        self.login.username = "roni"
        self.login.password = "12345"
        self.assertEqual(self.login.validate(), {})

    def test_validate_incorrect(self):
        self.login.username = "roni"
        self.login.password = "12"
        self.assertEqual(
            self.login.validate(),
            {"password": ["Password must be at least 4 characters long"]},
        )

    def test_open_menu(self):
        self.login.open_menu()
        self.assertEqual(self.login.game.open_menu_called, 1)

    def test_open_register(self):
        self.login.open_register()
        self.assertEqual(self.login.game.open_register_called, 1)

    def test_login_correct(self):
        self.login.username = "roni"
        self.login.password = "12345"
        self.login.login()
        self.assertEqual(self.login.game.user, True)

    def test_login_username_taken(self):
        self.login.username = "username_that_is_not_in_database"
        self.login.password = "12345"
        self.assertEqual(self.login.login(), {
                         "login": "Username or password invalid"})
