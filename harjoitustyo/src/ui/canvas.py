import pygame

from ui.views.menu_view import MenuView
from ui.views.sudoku_view import SudokuView
from ui.views.login_view import LoginView
from ui.views.register_view import RegisterView

from utils.resolution import get_lower_res, get_font_size

# Game canvas, handles UI elements


class Canvas:
    """Luokka, joka hallitsee käyttöliittymätoiminnallisuuksia

    Attributes:
        screen: Pygame screen -luokka
        screen_dimensions: Peli-ikkunan koko [x, y]
        buttons: Käyttöliittymällä olevat napit
        textboxes: Käyttöliittymällä olevat syötelaatikot
        focused_textbox: Käyttöliittymällä oleva valittu syötelaatikko
        lower_screen_dimension: Peli-ikkunan pienempi akseli x/y
        font_size: Käyttöliittymän universaali fonttikoko
        service_view: Palvelun näkymäluokka
    """

    def __init__(self, screen, screen_dimensions):
        """Luokan konstruktori,

        Args:
            screen: Pygame screen -luokka
            screen_dimensions: Peli-ikkunan koko [x, y]
        """

        self.screen = screen
        self.screen_dimensions = screen_dimensions

        self.buttons = []
        self.textboxes = []
        self.focused_textbox = None

        self.lower_screen_dimension = get_lower_res(self.screen_dimensions)
        self.font_size = get_font_size(self.lower_screen_dimension)

        self.service_view = None

    def set_service(self, service):
        """Asettaa käytetyn palvelunäkymän peliluokan palvelun mukaisesti

        Args:
            service: Palveluluokka, jonka mukaan asettaa palvelunäkymä
        """

        # Service has changed, update view
        self.buttons = []
        self.textboxes = []
        self.focused_textbox = None

        name = service.__name__()
        if name == "Menu":
            self.service_view = MenuView(self, service)
        elif name == "Sudoku":
            self.service_view = SudokuView(self, service)
        elif name == "Login":
            self.service_view = LoginView(self, service)
        elif name == "Register":
            self.service_view = RegisterView(self, service)

    def tick(self):
        """Päivittää käyttöliittymän"""

        # Background color
        self.screen.fill((255, 255, 255))

        self.service_view.tick()

        # Draw the display
        pygame.display.flip()

    def add_button(self, button: "Button"):
        """Lisää napin käyttöliittymään"""

        self.buttons.append(button)

    def add_textbox(self, textbox: "Textbox"):
        """Lisää syötelaatikon käyttöliittymään"""

        self.textboxes.append(textbox)

    def remove_button(self, button: "Button"):
        """Poistaa napin käyttöliittymästä"""

        self.buttons.remove(button)

    def handle_click(self, event: "Event"):
        """Käsittelee klikkauksen käyttöliittymällä

        Args:
            event: Pygame -klikkaustapahtuma
        """

        if event.button == 1:  # Left click
            for button in self.buttons:
                if button.is_over(event.pos):
                    button.click()

            if self.focused_textbox:
                self.focused_textbox.unset_focus()
                self.focused_textbox = None

            for textbox in self.textboxes:
                if textbox.is_over(event.pos):
                    textbox.set_focus()
                    self.focused_textbox = textbox

    def handle_text_input(self, event: "Event"):
        """Käsittelee tekstisyötteen käyttöliittymällä

        Args:
            event: Pygamen -tekstisyötetapahtuma
        """

        if self.focused_textbox:
            if event.key == pygame.K_BACKSPACE:
                self.focused_textbox.delete_char()
            else:
                self.focused_textbox.write_char(event.unicode)

    def update_screen_dimensions(self, event):
        """Päivittää ikkunan koon

        Args:
            event: Pygame VIDEORESIZE -tapahtuma
        """

        self.screen_dimensions[0] = event.w
        self.screen_dimensions[1] = event.h

        self.lower_screen_dimension = get_lower_res(self.screen_dimensions)
        self.font_size = get_font_size(self.lower_screen_dimension)
