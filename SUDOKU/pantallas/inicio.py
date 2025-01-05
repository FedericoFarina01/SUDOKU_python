import pygame
from botones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

# Cargar imágenes
img_pygame = pygame.image.load("SUDOKU/imagenes/pygame.png")
img_pygame = pygame.transform.scale(img_pygame, (400, 250))

img_fondo = pygame.image.load("SUDOKU/imagenes/marco.jpg")
img_fondo = pygame.transform.scale(img_fondo, (1000, 800))


def dibujar_pantalla_inicio(pantalla, dificultad):
    """
    Dibuja los elementos que se muestran en la pantalla de inicio

    Parametros:
        pantalla: Representa la pantalla donde se dibujan los elementos

    """

    pantalla.fill((255, 255, 255))  # Fondo blanco
    pantalla.blit(img_fondo, (-100, -100))
    pantalla.blit(img_pygame, (160, 0))
    # Dibujar botones
    dibujar_boton_jugar(pantalla)
    dibujar_boton_dificultad(pantalla, dificultad)
    dibujar_boton_puntajes(pantalla)
    dibujar_boton_salir(pantalla)
    titulo_sudoku(pantalla)



def titulo_sudoku(pantalla):
    """
    Dibuja el titulo del juego en pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibujan los elementos
    """
    fuente = pygame.font.SysFont("Arial", 30, bold=True)
    sombra_sudoku = fuente.render("S_U_D_O_K_U:", True, (0, 0, 0))
    texto_sudoku = fuente.render("S_U_D_O_K_U:", True, (0, 0, 0))
    pantalla.blit(sombra_sudoku, (532, 140)) 
    pantalla.blit(texto_sudoku, (530, 138)) 


def cambiar_dificultad(dificultad):
    """
    Cambia la dificultad del juego segun la opcion seleccionada

    Parametros:
        difdicultad: Indica la dificultad del juego que definira la cantidad de celdas a ocultar
    """
    if dificultad == "Facil":
        return "Medio"
    elif dificultad == "Medio":
        return "Dificil"
    elif dificultad == "Dificil":
        return "Facil"


