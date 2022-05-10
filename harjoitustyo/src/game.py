import pygame
from services.menu import Menu
from services.sudoku import Sudoku
from services.login import Login
from services.register import Register


class Game:
    """Luokka, joka hallitsee koko ohjelman tilaa

    Attributes:
        canvas: Canvas -luokan referenssi
        event_queue: EventQueue -luokan referenssi, joka palauttaa pygame.event.get() -tapahtumat
        clock: Pygamen kelloluokan referenssi, hallitsee pelin renderöinnin ajoitusta
        database: Käytetyn tietokantaluokan referenssi
        sudoku_folder_path: Sudokukansion polku

        user: Kirjautuneen käyttäjän tiedot, None jos käyttäjä ei ole kirjautunut
        service: Tämänhetkisen näkymän palveluluokka (menu, login, sudoku, ...)
    """

    def __init__(self, canvas, event_queue, clock, database, sudoku_folder_path):
        """Luokan konstruktori, asettaa näkymäksi päävalikon

        Args:
            canvas: Canvas -luokan referenssi
            event_queue: EventQueue -luokan referenssi, joka palauttaa pygame.event.get() -tapahtumat
            clock: Pygamen kelloluokan referenssi, hallitsee pelin renderöinnin ajoitusta
            database: Käytetyn tietokantaluokan referenssi
            sudoku_folder_path: Sudokukansion polku
        """

        self.canvas = canvas
        self.event_queue = event_queue
        self.clock = clock
        self.database = database
        self.sudoku_folder_path = sudoku_folder_path
        self.user = None

        self.set_service(Menu(self, self.database, sudoku_folder_path))

    def set_service(self, service):
        """Päivittää käytetyn palveluluokan tänne ja Canvas -luokalle

        Args:
            service: Uusi palveluluokka
        """

        self.service = service
        self.canvas.set_service(service)

    def start_loop(self):
        """Aloittaa pelisilmukan"""

        while True:
            if self.handle_events() is False:
                break

            self.update_canvas()
            self.clock.tick(60)

    def handle_events(self):
        """Käsittelee tapahtumat

        Returns:
            True, jos kaikki OK
            False, jos peli sammutetaan
        """

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
                self.canvas.handle_text_input(event)
            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.canvas.handle_click(event)
            # Window resize event
            if event.type == pygame.VIDEORESIZE:
                self.canvas.update_screen_dimensions(event)
        return True

    def update_canvas(self):
        """Kutsuu Canvas -lukan tick() -funktiota"""

        # Call UI functions
        self.canvas.tick()

    def open_sudoku(self, name):
        """Avaa sudokun

        Args:
            name: Sudokun nimi
        """

        self.set_service(Sudoku(self, self.sudoku_folder_path, name))

    def open_menu(self):
        """Avaa päävalikon"""

        self.set_service(Menu(self, self.database, self.sudoku_folder_path))

    def open_login(self):
        """Avaa kirjautumisnäkymän"""

        self.set_service(Login(self))

    def open_register(self):
        """Avaa rekisteröitymisnäkymän"""

        self.set_service(Register(self))

    def logout(self):
        """Kirjaa käyttäjän ulos"""

        self.user = None
