import pygame
from services.menu import Menu
from services.sudoku import Sudoku
from services.login import Login
from services.register import Register


class Game:
    def __init__(self, canvas, event_queue, clock, database):
        self.canvas = canvas
        self.event_queue = event_queue
        self.clock = clock
        self.database = database
        self.user = None

        self.set_service(Menu(self))

    def set_service(self, service):
        self.service = service
        self.canvas.set_service(service)

    def start_loop(self):
        while True:
            if self.handle_events() is False:
                break

            self.update_canvas()
            self.clock.tick(60)

    def handle_events(self):
        # Pygame event handling
        for event in self.event_queue.get():
            # Quit events
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                # Quit with ESC key
                if event.key == pygame.K_ESCAPE:
                    return False
                # Text input
                else:
                    self.canvas.handle_text_input(event)
            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.canvas.handle_click(event)
            # Window resize event
            if event.type == pygame.VIDEORESIZE:
                self.canvas.update_screen_dimensions(event)
        return True

    def update_canvas(self):
        # Background color
        self.canvas.screen.fill((255, 255, 255))

        # Call UI functions
        self.canvas.tick()

        # Draw the display
        pygame.display.flip()

    def open_sudoku(self, name):
        self.set_service(Sudoku(name, self))

    def open_menu(self):
        self.set_service(Menu(self))

    def open_login(self):
        self.set_service(Login(self))

    def open_register(self):
        self.set_service(Register(self))

    def logout(self):
        self.user = None
