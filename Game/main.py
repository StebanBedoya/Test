import pygame
import random
from jugador import Jugador
from enemigo import Enemigo, EnemigoSaltador
from bloque import Bloque
from funciones_basicas import (
    mostrar_mensaje_perdido,
    reiniciar_juego,
    crear_enemigos_y_nubes,
)
from menu import menu

pygame.init()

ancho_ventana, alto_ventana = 900, 600
pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana), pygame.NOFRAME)
pygame.display.set_caption("Juego al estilo Mario")
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 74)
pausado = False
mostrar_menu_salir = False
escenario_actual = 1
max_escenarios = 3
bloques_aparecieron = False
ganaste = False
COLORES = {"Rojo": (255, 0, 0), "Azul": (0, 0, 255), "Blanco": (255, 255, 255)}
color_seleccionado = menu(pantalla, fuente, COLORES)
jugador = Jugador(color_seleccionado)
montañas = [pygame.Rect(50, 400, 300, 200), pygame.Rect(550, 400, 300, 200)]

enemigos, nubes = crear_enemigos_y_nubes(escenario_actual)
bloques = (
    [Bloque(random.randint(100, 700), 400, contiene_powerup=True)]
    if escenario_actual == 1
    else []
)
bandera = pygame.Rect(800, 450, 20, 100) if escenario_actual == max_escenarios else None
ejecutando = True


def mostrar_menu_salir_fn():
    pantalla.fill((0, 0, 0))
    continuar = fuente.render("Continuar", True, (255, 255, 255))
    salir = fuente.render("Salir", True, (255, 255, 255))
    pantalla.blit(continuar, (350, 200))
    pantalla.blit(salir, (350, 400))
    pygame.display.flip()


def mostrar_ganador_fn():
    pantalla.fill((0, 0, 0))
    ganar = fuente.render("¡Ganaste!", True, (255, 255, 255))
    salir = fuente.render("Salir", True, (255, 255, 255))
    pantalla.blit(ganar, (350, 200))
    pantalla.blit(salir, (350, 400))
    pygame.display.flip()


while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.saltar()
            elif evento.key == pygame.K_ESCAPE:
                mostrar_menu_salir = not mostrar_menu_salir

        if mostrar_menu_salir and evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if 350 <= x <= 550 and 200 <= y <= 250:
                mostrar_menu_salir = False 
            elif 350 <= x <= 550 and 400 <= y <= 450:
                ejecutando = False 

    if ganaste:
        mostrar_ganador_fn()
        esperando_respuesta = True
        while esperando_respuesta:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = evento.pos
                    if 350 <= x <= 550 and 400 <= y <= 450:
                        pygame.quit()
                        exit()

    if not mostrar_menu_salir:
        if not pausado:
            teclas = pygame.key.get_pressed()
            jugador.mover(teclas)
            if not jugador.en_suelo:
                jugador.caer()

            for enemigo in enemigos:
                if jugador.rect.colliderect(enemigo.rect.inflate(-10, -10)):
                    mostrar_mensaje_perdido(pantalla, fuente)
                    jugador = reiniciar_juego(Jugador, color_seleccionado)
                    jugador.escenario_transicionado = False
                    enemigos, nubes = crear_enemigos_y_nubes(escenario_actual)

                    if escenario_actual == 1:
                        bloques = [
                            Bloque(random.randint(100, 700), 400, contiene_powerup=True)
                        ]

            if jugador.rect.x == 0 and jugador.escenario_transicionado:
                escenario_actual += 1
                if escenario_actual > max_escenarios:
                    ganaste = True
                else:
                    enemigos, nubes = crear_enemigos_y_nubes(escenario_actual)
                    bloques = (
                        [Bloque(random.randint(100, 700), 400, contiene_powerup=True)]
                        if escenario_actual == 1
                        else []
                    )
                    bandera = (
                        pygame.Rect(800, 450, 20, 100)
                        if escenario_actual == max_escenarios
                        else None
                    )
                    jugador.escenario_transicionado = False

            pantalla.fill((135, 206, 235))
            for montaña in montañas:
                pygame.draw.polygon(
                    pantalla,
                    (139, 69, 19),
                    [
                        (montaña.x, montaña.y + montaña.height),
                        (montaña.x + montaña.width // 2, montaña.y),
                        (montaña.x + montaña.width, montaña.y + montaña.height),
                    ],
                )
            for nube in nubes:
                pygame.draw.rect(pantalla, (255, 255, 255), nube)
            pygame.draw.rect(pantalla, (210, 105, 30), (0, 540, 900, 60))
            pygame.draw.rect(pantalla, color_seleccionado, jugador.rect)
            for enemigo in enemigos:
                enemigo.mover()
                if isinstance(enemigo, EnemigoSaltador):
                    pygame.draw.rect(
                        pantalla,
                        (0, 255, 0),
                        (
                            enemigo.rect.x,
                            enemigo.rect.y,
                            enemigo.rect.width,
                            enemigo.rect.height // 2,
                        ),
                    )
                    pygame.draw.rect(
                        pantalla,
                        (255, 255, 255),
                        (
                            enemigo.rect.x,
                            enemigo.rect.y + enemigo.rect.height // 2,
                            enemigo.rect.width,
                            enemigo.rect.height // 2,
                        ),
                    )
                else:
                    pygame.draw.rect(pantalla, enemigo.color, enemigo.rect)
            for bloque in bloques:
                pygame.draw.rect(pantalla, (0, 255, 0), bloque.rect)
                if jugador.rect.colliderect(bloque.rect):
                    if bloque.contiene_powerup:
                        jugador.super_salto_activo = True
                        bloques.remove(bloque)
            if bandera:
                pygame.draw.rect(pantalla, (255, 0, 0), bandera)
                if jugador.rect.colliderect(bandera):
                    ganaste = True
        else:
            mostrar_menu_salir_fn()
    else:
        mostrar_menu_salir_fn()

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
