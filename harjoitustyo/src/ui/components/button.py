import pygame
from ui.components.text import render, blit

# General button class to be used with Canvas UI


class Button:
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

    def update_text(self, text: str) -> None:
        self.text = text

    def update_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def update_size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def update_func(self, func) -> None:
        self.func = func

    def update_args(self, *args) -> None:
        self.args = args

    def draw(self) -> None:
        if self.outline:
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

        pygame.draw.rect(
            self.canvas.screen, self.color, (self.x, self.y, self.width, self.height), 0
        )

        if self.text != "":
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
