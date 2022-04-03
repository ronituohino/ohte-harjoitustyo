import pygame

# General button class to be used with Canvas UI


class Button():
    def __init__(self, canvas: "Canvas", color, x: int, y: int, width: int, height: int, text: str, font_size: int, outline: tuple, func, *args) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        # Outline defined as ((r:int,g:int,b:int), thickness:int)
        self.outline = outline
        self.func = func
        self.args = args

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

    def update_font_size(self, font_size: int) -> None:
        self.font_size = font_size

    def update_func(self, func) -> None:
        self.func = func

    def update_args(self, *args) -> None:
        self.args = args

    def draw(self, screen) -> None:
        if self.outline:
            pygame.draw.rect(screen, self.outline[0], (self.x - self.outline[1], self.y - self.outline[1],
                             self.width + self.outline[1] * 2, self.height + self.outline[1] * 2))

        pygame.draw.rect(screen, self.color, (self.x, self.y,
                         self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                               self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos: tuple) -> bool:
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def click(self) -> None:
        self.func(*self.args)
