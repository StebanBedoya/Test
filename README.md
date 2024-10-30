# Test Juego Python con libreria Pygame

Este es un sencillo juego al estilo de Mario desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es navegar a través de varios escenarios, evitar enemigos y recoger un power-up. Al alcanzar el tercer escenario, el jugador encontrará una meta que, al tocarla, indicará que el jugador ha ganado.

## Funcionalidades del Juego

- **Movimiento del Jugador**: El jugador puede moverse hacia la izquierda y derecha utilizando las teclas de flecha o `A` y `D`.
- **Salto del Jugador**: El jugador puede saltar utilizando la barra espaciadora.
- **Enemigos**: Hay dos tipos de enemigos:
  - **Enemigo Normal**: De color marrón, se mueve horizontalmente.
  - **Enemigo Saltador**: Mitad superior verde y mitad inferior blanca, se mueve horizontalmente y salta aleatoriamente.
- **Power-up**: Un único bloque de power-up aparece aleatoriamente en el mapa y otorga un súper salto al jugador.
- **Escenarios**: El juego consta de tres escenarios que cambian cuando el jugador alcanza el lado derecho de la pantalla. Los enemigos y nubes se generan aleatoriamente en cada nuevo escenario, asi mismo tiene montañas de fondo que siempre son las mismas alegando a la distancia y la perspectiva.
- **Meta**: En el tercer escenario, hay una meta que indica que el jugador ha ganado al tocarla.
- **Pausa y Menú**: El jugador puede pausar el juego y acceder al menú de opciones pulsando la tecla `Escape`.

## Cómo Jugar

1. **Movimiento**:
   - Usa las teclas de flecha izquierda (`<-`) y derecha (`->`) o `A` y `D` para mover al jugador.
   - Usa la barra espaciadora para saltar.
2. **Evitar Enemigos**: Evita colisionar con los enemigos para no perder.
3. **Recoger Power-up**: Recoge el bloque de power-up para activar el súper salto.
5. **Ganar el Juego**: Alcanza la meta en el tercer escenario para ganar.

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. Clona este repositorio:
   ```sh
   https://github.com/StebanBedoya/Test
