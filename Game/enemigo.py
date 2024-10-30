import pygame
import random


class Enemigo:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.velocidad_x = -3
        self.color = (252, 197, 37)

    def mover(self):
        self.rect.x += self.velocidad_x
        if self.rect.x < 0 or self.rect.x > 760:
            self.velocidad_x *= -1


class EnemigoSaltador:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.velocidad_x = random.choice([-3, 3])
        self.salto = -10
        self.en_salto = False

    def mover(self):
        self.rect.x += self.velocidad_x
        if self.rect.x < 0 or self.rect.x > 760:
            self.velocidad_x *= -1
        if not self.en_salto:
            if random.randint(0, 100) < 2:
                self.en_salto = True
        else:
            self.rect.y += self.salto
            self.salto += 1
            if self.rect.y >= 510:
                self.rect.y = 510
                self.en_salto = False
                self.salto = -10
