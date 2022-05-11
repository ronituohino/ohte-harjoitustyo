import pygame
from ui.components.text import render, blit


class Textbox:
    """Syötekenttäluokka, jolla voimme ottaa näppäimistön syötettä lomakkeisiin

    Attributes:
        canvas: Canvas luokka
        form: Syötekenttiä hallinnoiva lomake
        name: Syötekentän nimi (virheidenkäsittelyyn)
        color: Napin taustan väri
        x: Napin vasemman ylänurkan x-koordinaatti
        y: Napin vasemman ylänurkan y-koordinaatti
        width: Napin leveys
        height: Napin korkeus
        max_chars: Syötteen maksimipituus
        placeholder: Teksti joka näytetään jos kenttä on tyhjä
        placeholder: Tyhjän syötekentän tekstin väri
        outline: Napin rajaus ((r, g, b), paksuus)
        update_func: Funktio jota kutsutaan kun syöte muuttuu
    """

    def __init__(
        self,
        canvas: "Canvas",
        form: "Form",
        name: str,
        color: tuple,
        x: int,
        y: int,
        width: int,
        height: int,
        max_chars: int,
        placeholder: str,
        placeholder_color: tuple,
        outline: tuple,
        update_func,
    ):
        """Luokan konstruktori

        Args:
            canvas: Canvas luokka
            form: Syötekenttiä hallinnoiva lomake
            name: Syötekentän nimi (virheidenkäsittelyyn)
            color: Napin taustan väri
            x: Napin vasemman ylänurkan x-koordinaatti
            y: Napin vasemman ylänurkan y-koordinaatti
            width: Napin leveys
            height: Napin korkeus
            max_chars: Syötteen maksimipituus
            placeholder: Teksti joka näytetään jos kenttä on tyhjä
            placeholder: Tyhjän syötekentän tekstin väri
            outline: Napin rajaus ((r, g, b), paksuus)
        """

        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_chars = max_chars
        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        # Outline defined as ((r:int,g:int,b:int), thickness:int)
        self.outline = outline
        self.update_func = update_func

        self.canvas = canvas
        self.form = form
        self.canvas.add_textbox(self)
        self.value = None
        self.errors = None
        self.focus = False

    def is_over(self, pos: tuple) -> bool:
        """Tarkistaa onko pos syötekentän päällä, käytetään hiirivalinnan yhteydessä

        Args:
            pos: hiiren sijainti

        Returns:
            True, jos pos on kentän päällä
            False, jos ei
        """

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def set_focus(self):
        """Asettaa syötekentän fokusoiduksi kentäksi"""

        self.focus = True

    def unset_focus(self):
        """Asettaa syötekentän ei-fokusoiduksi kentäksi"""

        self.focus = False

    def write_char(self, char):
        """Kirjoittaa symbolin syötekenttään

        Args:
            char: Kirjoitettava merkki
        """

        if self.value:
            if not self.max_chars or len(self.value) < self.max_chars:
                self.value += char
                self.update()
        else:
            self.value = char
            self.update()

    def delete_char(self):
        """Poistaa viimeisen merkin syötekentästä"""

        if self.value:
            if len(self.value) > 1:
                self.value = self.value[:-1]
            else:
                self.value = None
            self.update()

    def update(self):
        """Kutsuu syötekentän päivitysfunktiota ja validoi lomakkeen"""

        self.update_func(self.value)
        self.form.validate()

    def set_errors(self, errors):
        """Asettaa syötekentän virheviestit"""

        self.errors = errors

    def update_position(self, x: int, y: int) -> None:
        """Päivittää syötekentän sijainnin

        Args:
            x: uusi x-koordinaatti
            y: uusi y-koordinaatti
        """

        self.x = x
        self.y = y

    def update_size(self, width: int, height: int) -> None:
        """Päivittää syötekentän koon

        Args:
            width: uusi leveys
            height: uusi korkeus
        """

        self.width = width
        self.height = height

    def draw(self):
        """Piirtää syötekentän"""

        if self.outline:
            self._draw_outline()

        self._draw_background()

        if self.value:
            self._draw_text()
        else:
            self._draw_placeholder()

        if self.errors and len(self.errors) > 0:
            self._draw_error_message()

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
        ren = render(self.value, (0, 0, 0), self.canvas.font_size)
        blit(
            self.canvas,
            self.x + self.width * 0.02,
            self.y + (self.height / 2 - ren.get_height() / 2),
            ren,
        )

    def _draw_placeholder(self):
        ren = render(self.placeholder, self.placeholder_color, self.canvas.font_size)
        blit(
            self.canvas,
            self.x + self.width * 0.02,
            self.y + (self.height / 2 - ren.get_height() / 2),
            ren,
        )

    def _draw_error_message(self):
        ren = render(self.errors[0], (200, 0, 0), self.canvas.font_size * 0.5)
        blit(
            self.canvas,
            self.x,
            self.y + self.height + ren.get_height() / 2,
            ren,
        )
