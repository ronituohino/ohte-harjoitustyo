import pygame
from ui.components.text import render, blit


class Textbox:
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
            if not self.max_chars or len(self.value) < self.max_chars:
                self.value += char
                self.update()
        else:
            self.value = char
            self.update()

    def delete_char(self):
        if self.value:
            if len(self.value) > 1:
                self.value = self.value[:-1]
            else:
                self.value = None
            self.update()

    def update(self):
        self.update_func(self.value)
        self.form.validate()

    def set_errors(self, errors):
        self.errors = errors

    def update_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def update_size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def draw(self):
        # Outline
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

        # Main rect
        pygame.draw.rect(
            self.canvas.screen, self.color, (self.x, self.y, self.width, self.height), 0
        )

        # Text in rect (value / placeholder)
        if self.value:
            ren = render(self.value, (0, 0, 0), self.canvas.font_size)
            blit(
                self.canvas,
                self.x + self.width * 0.02,
                self.y + (self.height / 2 - ren.get_height() / 2),
                ren,
            )
        else:
            ren = render(
                self.placeholder, self.placeholder_color, self.canvas.font_size
            )
            blit(
                self.canvas,
                self.x + self.width * 0.02,
                self.y + (self.height / 2 - ren.get_height() / 2),
                ren,
            )

        # Error message
        if self.errors and len(self.errors) > 0:
            ren = render(self.errors[0], (200, 0, 0), self.canvas.font_size * 0.5)
            blit(
                self.canvas,
                self.x,
                self.y + self.height + ren.get_height() / 2,
                ren,
            )
