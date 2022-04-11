import pygame
from ui.canvas import Canvas
from game import Game
from event_queue import EventQueue

# Main init
pygame.init()

# Config
screen_dimensions = [1000, 600]

# Set up the drawing window
screen = pygame.display.set_mode(screen_dimensions, pygame.RESIZABLE)
pygame.display.set_caption("Sudoku")

game = Game(Canvas(screen, screen_dimensions),
            EventQueue(), pygame.time.Clock())
game.start_loop()

pygame.quit()
