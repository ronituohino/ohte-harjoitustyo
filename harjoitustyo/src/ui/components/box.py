import pygame


def box(canvas: "Canvas", color, x, y, width, height):
    """Piirtää suorakulmion näytölle

    Args:
        color: Suorakulmion väri
        x: Suorakulmion vasemman ylänurkan x-koordinaatti
        y: Suorakulmion vasemman ylänurkan y-koordinaatti
        width: Suorakulmion leveys
        height: Suorakulmion korkeus
    """
    pygame.draw.rect(
        canvas.screen,
        color,
        (
            x,
            y,
            width,
            height,
        ),
    )


def box_outlined(canvas: "Canvas", color, x, y, width, height, outline):
    """Piirtää rajatun suorakulmion näytölle

    Args:
        color: Suorakulmion väri
        x: Suorakulmion vasemman ylänurkan x-koordinaatti
        y: Suorakulmion vasemman ylänurkan y-koordinaatti
        width: Suorakulmion leveys
        height: Suorakulmion korkeus
        outline: ((r, g, b): rajan väri, rajan paksuus, rajan ja tekstin etäisyys)
    """

    pygame.draw.rect(
        canvas.screen,
        outline[0],
        (
            x - outline[1] - outline[2],
            y - outline[1] - outline[2],
            width + (outline[1] + outline[2]) * 2,
            height + (outline[1] + outline[2]) * 2,
        ),
    )

    pygame.draw.rect(
        canvas.screen,
        color,
        (
            x - outline[2],
            y - outline[2],
            width + outline[2] * 2,
            height + outline[2] * 2,
        ),
    )
