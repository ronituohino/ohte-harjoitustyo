import pygame
from sudoku import Sudoku
from canvas import Canvas

# Main init
pygame.init()

# Config
running = True
screen_dimensions = [1000, 600]
canvas = Canvas()

# Set up the drawing window
screen = pygame.display.set_mode(screen_dimensions, pygame.RESIZABLE)
s = Sudoku("dots.sudoku", canvas, screen_dimensions)

# More Pygame setup
clock = pygame.time.Clock()
pygame.display.set_caption("Sudoku")

while running:
    # Window close button event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            canvas.handle_click(event)
        if event.type == pygame.VIDEORESIZE:
            screen_dimensions[0] = event.w
            screen_dimensions[1] = event.h

    screen.fill((255, 255, 255))

    s.tick(screen, screen_dimensions)

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
