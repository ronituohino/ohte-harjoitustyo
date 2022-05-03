import pygame


def box(canvas: "Canvas", color, x, y, width, height, outline):
    if outline is not None:
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
    else:
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
