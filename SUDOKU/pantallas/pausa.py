import pygame
from botones import dibujar_boton_reanudar

def dibujar_pantalla_pausa(pantalla, ancho_pantalla, largo_pantalla):
    """
    Dibuja los elementos que se muestran en la pantalla de pausa

    Parametros:
        pantalla: Representa la pantalla donde se dibujan los elementos
        ancho_pantalla: Representa el ancho de la pantalla
        largo_pantalla: Representa el largo de la pantalla

    """
    pantalla.fill((50, 50, 50))  # Fondo gris oscuro
    fuente = pygame.font.SysFont("Arial", 50, bold=True)
    texto_pausa = fuente.render("Juego en Pausa", True, (255, 255, 255))
    texto_x = ancho_pantalla // 2 - texto_pausa.get_width() // 2
    texto_y = largo_pantalla // 2 - texto_pausa.get_height() // 2
    dibujar_boton_reanudar(pantalla)
    pantalla.blit(texto_pausa, (texto_x, texto_y))