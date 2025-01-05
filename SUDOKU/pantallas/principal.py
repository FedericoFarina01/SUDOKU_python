import pygame
from botones import *
from funciones import *

# Tamaños y ubicaciones: X, Y
ancho_pantalla = 800
largo_pantalla = 600
dimension_pantalla = (ancho_pantalla, largo_pantalla)

img_fondo = pygame.image.load("SUDOKU/imagenes/marco.jpg")
img_fondo = pygame.transform.scale(img_fondo, (1000, 800))


# Creación de una pantalla
pantalla = pygame.display.set_mode(dimension_pantalla)

def dibujar_pantalla_principal(pantalla, tiempo_inicio, cant_errores):
    """
    Dibuja los elementos que se muestran en la pantalla principal del juego

    Parametros:
        pantalla: Representa la pantalla donde se dibujan los elementos
        tiempo_inicio: Representa el momento en que arranca el contador de tiempo
        cant_errores: Representa la cantidad de errores cometidos

    """
    pantalla.blit(img_fondo, (-100, -100))
    dibujar_boton_volver(pantalla) 
    dibujar_boton_reiniciar(pantalla)
    dibujar_boton_pausa(pantalla)
    dibujar_errores(pantalla, cant_errores)
    dibujar_tiempo(pantalla, tiempo_inicio)
    pygame.mixer.music.stop()

#--------------------------------------------------------------------------------
    
