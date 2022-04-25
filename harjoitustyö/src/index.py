import sys
import os
import pygame
from ui.canvas import Canvas
from game import Game
from services.db import Database

# Main init
pygame.init()

# Config
screen_dimensions = [1000, 600]

# Set up the drawing window
screen = pygame.display.set_mode(screen_dimensions, pygame.RESIZABLE)
pygame.display.set_caption("Sudoku")

# Load up database
if len(sys.argv) > 1 and sys.argv[1] == "dev":
    db = Database(1)
    db.clear()
    db.create()
    db.sample_data()
else:
    db = Database(0)
    db.create()

# Event Queue definition
class EventQueue:
    def get(self):
        return pygame.event.get()


game = Game(
    Canvas(screen, screen_dimensions),
    EventQueue(),
    pygame.time.Clock(),
    db,
    f"{os.getcwd()}/sudokus",
)

game.start_loop()

pygame.quit()
