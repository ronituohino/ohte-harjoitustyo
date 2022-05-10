import unittest

from services.db import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(2)
        self.db.clear()
        self.db.create()

    def test_create_account(self):
        account = self.db.create_account("roni", "12345")
        self.assertEqual(
            account,
            {
                "id": 1,
                "username": "roni",
            },
        )

    def test_create_completed_data(self):
        self.db.create_account("roni", "12345")
        self.db.add_completed(1, "test1.sudoku", 123)
        self.assertEqual(self.db.get_completed_data(1), [("test1.sudoku", 123.0)])

    def test_set_menu_location(self):
        self.db.set_menu_location(2)
        self.assertEqual(self.db.get_menu_location(), 2)
