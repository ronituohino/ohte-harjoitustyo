import pygame
from ui.components.elements.element import Element


class Textbox(Element):
    def __init__(
        self,
        canvas: "Canvas",
        color: tuple,
        x: int,
        y: int,
        width: int,
        height: int,
        font_size: int,
        outline: tuple,
    ):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        # Outline defined as ((r:int,g:int,b:int), thickness:int)
        self.outline = outline

        self.canvas = canvas
        self.canvas.add_textbox(self)
        self.focus = False

    def is_over(self, pos: tuple) -> bool:
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def set_focus(self):
        self.focus = True

    def unset_focus(self):
        self.focus = False

    def write_char(self, char):
        if self.value:
            self.value += char
        else:
            self.value = char

    def delete_char(self):
        if self.value:
            if len(self.value) > 1:
                self.value = self.value[:-1]
            else:
                self.value = None

    def draw(self):
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

        if self.value and len(self.value) > 0:
            font = pygame.font.SysFont("comicsans", self.font_size)
            text = font.render(self.value, 1, (0, 0, 0))
            self.canvas.screen.blit(
                text,
                (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2),
                ),
            )
