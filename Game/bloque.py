import pygame


class Bloque:
    def __init__(self, x, y, contiene_powerup=False):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.contiene_powerup = contiene_powerup
        self.mostrado = False

    def revelar(self):
        if self.contiene_powerup:
            self.mostrado = True
