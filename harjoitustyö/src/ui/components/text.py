import pygame


def render(text: str, color: tuple, font_size: float):
    font = pygame.font.SysFont("comicsans", int(font_size))
    return font.render(text, 1, color)


def blit(canvas: "Canvas", x: int, y: int, render):
    canvas.screen.blit(
        render,
        (x, y),
    )


def text(canvas: "Canvas", text: str, x: int, y: int, color: tuple, font_size: float):
    blit(canvas, x, y, render(text, color, font_size))
