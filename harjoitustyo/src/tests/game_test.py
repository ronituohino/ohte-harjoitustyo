import unittest
import os

import pygame

from game import Game
from services.db import Database


class FakeCanvas:
    def __init__(self):
        self.set_service_called = 0
        self.tick_called = 0
        self.handle_click_called = 0
        self.handle_text_input_called = 0
        self.update_screen_dimensions_called = 0

    def set_service(self, service):
        self.set_service_called += 1

    def tick(self):
        self.tick_called += 1

    def handle_click(self, event: "FakeEvent"):
        self.handle_click_called += 1

    def handle_text_input(self, event: "FakeEvent"):
        self.handle_text_input_called += 1

    def update_screen_dimensions(self, event):
        self.update_screen_dimensions_called += 1


class FakeEventQueue:
    def __init__(self):
        self.event_queue = []

    def get(self):
        return self.event_queue

    def add(self, event):
        self.event_queue.append(event)


class FakeEvent:
    def __init__(self, type, key):
        self.type = type
        self.key = key


class FakeClock:
    def __init__(self):
        self.tick_called = 0

    def tick(self):
        self.tick_called += 1


# Test Game class functionality, but also app integration


class TestGame(unittest.TestCase):
    def setUp(self):
        db = Database(2)
        db.clear()
        db.create()
        db.sample_data()
        self.game = Game(
            FakeCanvas(),
            FakeEventQueue(),
            FakeClock(),
            db,
            f"{os.getcwd()}/src/tests/test_sudokus",
        )

    def test_service_name(self):
        self.assertEqual(self.game.service.__name__(), "Menu")

    def test_open_sudoku(self):
        self.game.open_sudoku("test1")
        self.assertEqual(self.game.service.__name__(), "Sudoku")

    def test_open_login(self):
        self.game.open_login()
        self.assertEqual(self.game.service.__name__(), "Login")

    def test_open_register(self):
        self.game.open_register()
        self.assertEqual(self.game.service.__name__(), "Register")

    def test_event_handling(self):
        self.game.event_queue.add(FakeEvent(pygame.MOUSEBUTTONDOWN, 0))
        self.game.event_queue.add(FakeEvent(pygame.MOUSEBUTTONDOWN, 0))
        self.game.event_queue.add(FakeEvent(pygame.VIDEORESIZE, 0))
        self.game.event_queue.add(FakeEvent(pygame.QUIT, 0))

        self.game.start_loop()

        self.assertEqual(self.game.canvas.handle_click_called, 2)
        self.assertEqual(self.game.canvas.update_screen_dimensions_called, 1)

    def test_solve_sudoku(self):
        # Navigate to open test2.sudoku
        self.game.service.move_right()
        self.game.service.move_left()
        self.assertEqual(
            self.game.service.sudokus[self.game.service.selected_sudoku], "test2"
        )
        self.game.service.open_sudoku()

        # Place missing pieces
        self.game.service.set_selection_value(3)
        self.game.service.set_value((6, 1))

        self.game.service.set_selection_value(8)
        self.game.service.set_value((3, 2))

        self.game.service.set_selection_value(7)
        self.game.service.set_value((2, 5))

        self.assertEqual(self.game.service.solved, True)

    def test_registration(self):
        # Open login view
        self.game.service.open_login()

        # Click "new user?" -button
        self.game.service.open_register()

        self.game.service.username = "jare"
        self.game.service.password = "12345"
        self.game.service.password_again = "12345"
        self.game.service.register()

        self.assertEqual(self.game.user, {"id": 2, "username": "jare"})

    def test_login(self):
        self.game.service.open_login()

        self.game.service.username = "roni"
        self.game.service.password = "123qwe123"

        self.game.service.login()

        self.assertEqual(self.game.user, {"id": 1, "username": "roni"})

    def test_logout(self):
        # Log in first
        self.game.service.open_login()
        self.game.service.username = "roni"
        self.game.service.password = "123qwe123"
        self.game.service.login()

        self.game.service.logout()

        self.assertEqual(self.game.user, None)
