import pygame
# General button class to be used with Canvas UI


class Button():
    def __init__(self, canvas, color, x, y, width, height, text, func, *args):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.func = func
        self.args = args

        self.canvas = canvas
        canvas.add_button(self)

    def update_text(self, text):
        self.text = text

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_size(self, width, height):
        self.width = width
        self.height = height

    def update_func(self, func):
        self.func = func

    def update_args(self, *args):
        self.args = args

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y,
                         self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                               self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def click(self):
        self.func(*self.args)
