import unittest
from utils.validation import (
    username_validation,
    password_validation,
    password_again_validation,
)


class TestValidation(unittest.TestCase):
    def test_username_empty(self):
        err = username_validation("")
        # Username missing, must be at least 2 chars long
        self.assertEqual(len(err), 2)

    def test_username_too_short(self):
        err = username_validation("a")
        self.assertEqual(len(err), 1)  # Too short

    def test_username_ok(self):
        err = username_validation("jaakko")
        self.assertEqual(len(err), 0)  # OK

    def test_password_empty(self):
        err = password_validation("")
        # Password missing, must be at least 4 chars long
        self.assertEqual(len(err), 2)

    def test_password_too_short(self):
        err = password_validation("abc")
        self.assertEqual(len(err), 1)  # Too short

    def test_password_ok(self):
        err = password_validation("abcd")
        self.assertEqual(len(err), 0)  # OK

    def test_password_again_mismatch(self):
        err = password_again_validation("abc", "abd")
        self.assertEqual(len(err), 1)

    def test_password_again_match(self):
        err = password_again_validation("password123", "password123")
        self.assertEqual(len(err), 0)  # OK
