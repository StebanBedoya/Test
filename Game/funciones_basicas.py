import pygame
import random
from enemigo import Enemigo, EnemigoSaltador
from bloque import Bloque


def mostrar_pausa(pantalla, fuente):
    mensaje = fuente.render("Pausa", True, (255, 255, 255))
    pantalla.blit(
        mensaje,
        (
            pantalla.get_width() // 2 - mensaje.get_width() // 2,
            pantalla.get_height() // 2 - mensaje.get_height() // 2,
        ),
    )
    pygame.display.flip()


def dibujar_menu(pantalla, fuente, COLORES):
    pantalla.fill((0, 0, 0))
    titulo = fuente.render("Elige un color y presiona Iniciar", True, (255, 255, 255))
    pantalla.blit(titulo, (100, 50))
    for i, (nombre, color) in enumerate(COLORES.items()):
        color_texto = pygame.font.Font(None, 50).render(nombre, True, color)
        pantalla.blit(color_texto, (150, 150 + i * 100))
    boton_iniciar = pygame.font.Font(None, 50).render("Iniciar", True, (255, 255, 255))
    pantalla.blit(boton_iniciar, (350, 500))
    pygame.display.flip()


def reiniciar_juego(Jugador, color_seleccionado):
    jugador = Jugador(color_seleccionado)
    jugador.escenario_transicionado = False
    return jugador


def mostrar_mensaje_perdido(pantalla, fuente):
    mensaje = fuente.render("Has perdido", True, (255, 0, 0))
    pantalla.blit(
        mensaje,
        (
            pantalla.get_width() // 2 - mensaje.get_width() // 2,
            pantalla.get_height() // 2 - mensaje.get_height() // 2,
        ),
    )
    pygame.display.flip()
    pygame.time.delay(2000)


def crear_enemigos_y_nubes(escenario_actual):
    num_enemigos = random.randint(1, 2 + escenario_actual)
    enemigos = []
    zona_segura_x = 300
    min_distancia_entre_enemigos = 200
    max_intentos = 10 

    for _ in range(num_enemigos):
        intentos = 0
        while intentos < max_intentos:
            x = random.randint(zona_segura_x, 700)
            if all(
                abs(x - enemigo.rect.x) > min_distancia_entre_enemigos
                for enemigo in enemigos
            ):
                if random.choice([True, False]):
                    enemigos.append(Enemigo(x, 510))
                else:
                    enemigos.append(EnemigoSaltador(x, 510))
                break
            intentos += 1

    nubes = [
        pygame.Rect(random.randint(50, 750), random.randint(50, 200), 200, 60)
        for _ in range(escenario_actual)
    ]
    return enemigos, nubes
