import pygame
from ui.components.text import render, blit

# General button class to be used with Canvas UI


class Button:
    """Nappi, joka kutsuu sille annetun funktion argumenteilla

    Attributes:
        canvas: Canvas luokka
        color: Napin taustan väri
        x: Napin vasemman ylänurkan x-koordinaatti
        y: Napin vasemman ylänurkan y-koordinaatti
        width: Napin leveys
        height: Napin korkeus
        text: Napin teksti
        outline: Napin rajaus ((r, g, b), paksuus)
        func: Funktion viite
        *args: Funktiolle annetut argumentit
    """

    def __init__(
        self,
        canvas: "Canvas",
        color,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        outline: tuple,
        func,
        *args
    ) -> None:
        """Luokan konstruktori

        Args:
            canvas: Canvas luokka
            color: Napin taustan väri
            x: Napin vasemman ylänurkan x-koordinaatti
            y: Napin vasemman ylänurkan y-koordinaatti
            width: Napin leveys
            height: Napin korkeus
            text: Napin teksti
            outline: Napin rajaus ((r, g, b), paksuus)
            func: Funktion viite
            *args: Funktiolle annetut argumentit
        """

        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        # Outline defined as ((r:int,g:int,b:int), thickness:int)
        self.outline = outline
        self.func = func
        self.args = args
        self.return_val = None

        self.canvas = canvas
        canvas.add_button(self)

    def update_color(self, color) -> None:
        """Päivittää napin värin

        Args:
            color: uusi väri
        """

        self.color = color

    def update_text(self, text: str) -> None:
        """Päivittää napin tekstin

        Args:
            text: uusi teksti
        """

        self.text = text

    def update_position(self, x: int, y: int) -> None:
        """Päivittää napin sijainnin

        Args:
            x: uusi x-koordinaatti
            y: uusi y-koordinaatti
        """

        self.x = x
        self.y = y

    def update_size(self, width: int, height: int) -> None:
        """Päivittää napin koon

        Args:
            width: uusi leveys
            height: uusi korkeus
        """

        self.width = width
        self.height = height

    def update_func(self, func) -> None:
        """Päivittää napin funktion

        Args:
            func: uusi funktio
        """

        self.func = func

    def update_args(self, *args) -> None:
        """Päivittää napin funktion argumentit

        Args:
            *args: uuden argumentit
        """

        self.args = args

    def draw(self) -> None:
        """Piirtää napin"""

        if self.outline:
            self._draw_outline()

        self._draw_background()

        if self.text != "":
            self._draw_text()

    def _draw_outline(self):
        pygame.draw.rect(
            self.canvas.screen,
            self.outline[0],
            (
                self.x - self.outline[1],
                self.y - self.outline[1],
                self.width + self.outline[1] * 2,
                self.height + self.outline[1] * 2,
            ),
        )

    def _draw_background(self):
        pygame.draw.rect(
            self.canvas.screen, self.color, (self.x, self.y, self.width, self.height), 0
        )

    def _draw_text(self):
        ren = render(self.text, (0, 0, 0), self.canvas.font_size)
        blit(
            self.canvas,
            self.x + (self.width / 2 - ren.get_width() / 2),
            self.y + (self.height / 2 - ren.get_height() / 2),
            ren,
        )

    def is_over(self, pos: tuple) -> bool:
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def click(self) -> None:
        self.return_val = self.func(*self.args)
