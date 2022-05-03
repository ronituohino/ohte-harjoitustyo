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

    def handle_click(self, event: "Event"):
        self.handle_click_called += 1

    def handle_text_input(self, event: "Event"):
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
