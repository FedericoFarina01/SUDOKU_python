import pygame
from botones import dibujar_caja_texto
import json
from funciones import calcular_puntaje

def dibujar_pantalla_ganaste(pantalla, puntaje_final, nombre_jugador):
    """
    Dibuja los elementos que se muestran en la pantalla al ganar el Sudoku

    Parametros:
        pantalla: Representa la pantalla donde se dibujan los elementos
    
    Retorna:
        rect_caja: Representa el area de la caja de texto
    """

    # Fondo y título
    pantalla.fill((50, 50, 50))  
    fuente = pygame.font.SysFont("Arial", 50, bold=True)
    texto_ganaste = fuente.render("¡GANASTE!", True, (255, 255, 255))

    # Mostrar el puntaje final
    fuente_puntos = pygame.font.SysFont("Arial", 40, bold=True)
    texto_puntajes = fuente_puntos.render(f"Puntos: {int(puntaje_final)}", True, (0, 0, 0))

    # Dibuja los botones
    dibujar_boton_nueva_partida(pantalla) 
    dibujar_boton_ver_puntajes(pantalla) 

    # Dibujar la caja de texto
    rect_caja = dibujar_caja_texto(pantalla)

    # Mostrar el nombre del jugador dentro de la caja de texto
    fuente_caja = pygame.font.SysFont("Arial", 30)
    texto_nombre = fuente_caja.render(nombre_jugador, True, (0, 0, 0))

    pantalla.blit(texto_nombre, (rect_caja.x + 10, rect_caja.y + 5))
    pantalla.blit(texto_puntajes, (265, 200))
    pantalla.blit(texto_ganaste, (280, 30))

    return rect_caja 

#------------------------------------------------------------------------------------------------------------
def dibujar_boton_nueva_partida(pantalla):
    """
    Dibuja el boton nueva_partida en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_nueva_partida: Representa el area del boton 
    """
    x = 10
    y = 30
    ancho = 200
    alto = 40

    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_nueva_partida = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20) 
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_nueva_partida = fuente.render("Nueva partida", True, (0, 0, 0))
    pantalla.blit(texto_nueva_partida, (x + 20, y + 5))
    
    return rect_nueva_partida

#------------------------------------------------------------------------------------------------------------

def dibujar_boton_ver_puntajes(pantalla):
    """
    Dibuja el boton ver_puntajes en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_ver_puntajes: Representa el area del boton 
    """
    x = 600
    y = 30  
    ancho = 200
    alto = 40
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_ver_puntajes = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20) 
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_ver_puntajes = fuente.render("Ver puntajes", True, (0, 0, 0))
    pantalla.blit(texto_ver_puntajes, (x + 20, y + 5))
    
    return rect_ver_puntajes

#-------------------------------------------------------------------------------------------