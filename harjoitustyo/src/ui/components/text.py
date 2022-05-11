import pygame


def render(text: str, color: tuple, font_size: float):
    """Renderöi tekstin

    Args:
        text: Teksti
        color: Tekstin väri
        font_size: Fonttikoko

    Returns:
        Renderöintiobjektin, jonka voi piirtää näytölle blit -funktion avulla
    """

    font = pygame.font.SysFont("comicsans", int(font_size))
    return font.render(text, 1, color)


def blit(canvas: "Canvas", x: int, y: int, render):
    """Pirtää renderöidyn tekstin näytölle

    Args:
        canvas: Näyttö, jolle piirretään
        x: Tekstin vasemman yläkulman x-koordinaatti
        y: Tekstin vasemman yläkulman y-koordinaatti
        render: Renderöity teksti
    """

    canvas.screen.blit(
        render,
        (x, y),
    )


def text(canvas: "Canvas", text: str, x: int, y: int, color: tuple, font_size: float):
    """Piirtää tekstiä näytölle

    Args:
        canvas: Näyttö, jolle piirretään
        text: Teksti
        x: Tekstin vasemman yläkulman x-koordinaatti
        y: Tekstin vasemman yläkulman y-koordinaatti
        color: Tekstin väri
        font_size: Fonttikoko

    Returns:
        Renderöintiobjektin, jonka voi piirtää näytölle blit -funktion avulla
    """

    blit(canvas, x, y, render(text, color, font_size))
