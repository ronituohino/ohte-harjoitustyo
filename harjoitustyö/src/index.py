import pygame
from ui.canvas import Canvas

# Main init
pygame.init()

# Config
screen_dimensions = [1000, 600]

# Set up the drawing window
screen = pygame.display.set_mode(screen_dimensions, pygame.RESIZABLE)

# Init UI canvas
canvas = Canvas(screen, screen_dimensions)

# More Pygame setup
clock = pygame.time.Clock()
pygame.display.set_caption("Sudoku")
RUNNING = True

while RUNNING:
    # Pygame event handling
    for event in pygame.event.get():
        # Quit events
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            canvas.handle_click(event)
        # Window resize event
        if event.type == pygame.VIDEORESIZE:
            screen_dimensions[0] = event.w
            screen_dimensions[1] = event.h

    # Background color
    screen.fill((255, 255, 255))

    # Call UI functions
    canvas.tick(screen_dimensions)

    # Flip the display
    pygame.display.flip()

    # Limit framerate to 60
    clock.tick(60)

pygame.quit()
