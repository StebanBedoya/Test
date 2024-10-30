import pygame


def menu(pantalla, fuente, colores):
    mostrar_menu = True
    color_seleccionado = colores["Rojo"]

    while mostrar_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if 350 <= x <= 450 and 500 <= y <= 550:
                    mostrar_menu = False
                elif 150 <= x <= 350 and 150 <= y <= 200:
                    color_seleccionado = colores["Rojo"]
                elif 150 <= x <= 350 and 250 <= y <= 300:
                    color_seleccionado = colores["Azul"]
                elif 150 <= x <= 350 and 350 <= y <= 400:
                    color_seleccionado = colores["Blanco"]

        dibujar_menu(pantalla, fuente, colores)

    return color_seleccionado


def dibujar_menu(pantalla, fuente, colores):
    pantalla.fill((0, 0, 0))
    titulo = fuente.render("Elige un color y presiona Iniciar", True, (255, 255, 255))
    pantalla.blit(titulo, (100, 50))

    for i, (nombre, color) in enumerate(colores.items()):
        color_texto = pygame.font.Font(None, 50).render(nombre, True, color)
        pantalla.blit(color_texto, (150, 150 + i * 100))

    boton_iniciar = pygame.font.Font(None, 50).render("Iniciar", True, (255, 255, 255))
    pantalla.blit(boton_iniciar, (350, 500))
    pygame.display.flip()
