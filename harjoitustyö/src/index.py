import sys
import pygame
from ui.canvas import Canvas
from game import Game
from event_queue import EventQueue
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

game = Game(Canvas(screen, screen_dimensions), EventQueue(), pygame.time.Clock(), db)
game.start_loop()

pygame.quit()
