import pygame


class Jugador:
    def __init__(self, color):
        self.rect = pygame.Rect(100, 500, 40, 40)
        self.color = color
        self.velocidad_y = 0
        self.en_suelo = True
        self.velocidad_x = 5
        self.super_salto_activo = False
        self.escenario_transicionado = False  
    def mover(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidad_x
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidad_x

        if self.rect.x < 0:
            self.rect.x = 0

        if (
            self.rect.x + self.rect.width > 900
        ): 
            self.transicionar_a_nuevo_escenario()

        if not self.en_suelo:
            self.velocidad_y += 1
        self.rect.y += self.velocidad_y
        if self.rect.y >= 500:
            self.rect.y = 500
            self.en_suelo = True
            self.velocidad_y = 0

    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = -15 if not self.super_salto_activo else -20
            self.en_suelo = False

    def caer(self):
        if not self.en_suelo:
            self.rect.y += self.velocidad_y
            self.velocidad_y += 1

    def transicionar_a_nuevo_escenario(self):
        if not self.escenario_transicionado:
            print("Transicionando a un nuevo escenario...")
            self.rect.x = 0  
            self.escenario_transicionado = True 