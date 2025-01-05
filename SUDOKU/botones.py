import pygame


def dibujar_boton_jugar(pantalla) -> pygame.Rect :
    """
    Dibuja el boton jugar en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_jugar: Representa el area del boton jugar
    """
    x = 290
    y = 200
    ancho = 120
    alto = 55

    rect_jugar = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render("Jugar", True, (0, 0, 0))  
    texto_jugar = fuente.render("Jugar", True, (0, 0, 0))
    if rect_jugar.collidepoint(pygame.mouse.get_pos()):
        texto_jugar = fuente.render("Jugar", True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_jugar, (x + 15, y + 10))

    return rect_jugar

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_puntajes(pantalla) -> pygame.Rect:
    """
    Dibuja el boton puntajes en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_puntajes: Representa el area del boton puntajes
    """
    x = 290
    y = 270
    ancho = 160
    alto = 55

    rect_puntajes = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render("Puntajes", True, (0, 0, 0)) 
    texto_puntajes = fuente.render("Puntajes", True, (0, 0, 0))
    if rect_puntajes.collidepoint(pygame.mouse.get_pos()):
        texto_puntajes = fuente.render("Puntajes", True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_puntajes, (x + 15, y + 10))

    return rect_puntajes
#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_dificultad(pantalla, dificultad) -> pygame.Rect:
    """
    Dibuja el boton dificultad en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
        dificultad: Representa la dificultad del juego
    
    Retorna:
        rect_dificultad: Representa el area del boton dificultad
    """
    x = 290
    y = 340
    ancho = 110
    alto = 55

    rect_dificultad = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render(dificultad, True, (0, 0, 0))
    texto_dificultad = fuente.render(dificultad, True, (0, 0, 0))
    if rect_dificultad.collidepoint(pygame.mouse.get_pos()):
        texto_dificultad = fuente.render(dificultad, True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_dificultad, (x + 15, y + 10))

    return rect_dificultad
    
#----------------------------------------------------------------------------------
def dibujar_boton_salir(pantalla) -> pygame.Rect:
    """
    Dibuja el boton salir en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_salir: Representa el area del boton salir
    """
    x = 290
    y = 410
    ancho = 100
    alto = 55

    rect_salir = pygame.Rect(x, y, ancho, alto)
    fuente = pygame.font.SysFont("Arial", 40, bold=True)
    sombra = fuente.render("Salir", True, (0, 0, 0))
    texto_salir = fuente.render("Salir", True, (0, 0, 0))
    if rect_salir.collidepoint(pygame.mouse.get_pos()):
        texto_salir = fuente.render("Salir", True, (200, 143, 90))
        pantalla.blit(sombra, (x + 18, y + 12))
    pantalla.blit(texto_salir, (x + 15, y + 10))

    return rect_salir

#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_volver(pantalla) -> pygame.Rect:
    """
    Dibuja el boton volver en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_volver: Representa el area del boton volver
    """
    imagen_volver = pygame.image.load("SUDOKU/imagenes/flecha_volver.png")
    imagen_volver = pygame.transform.scale(imagen_volver, (50, 50))  

    x = 70
    y = 70
    
    rect_volver = pygame.Rect(x, y, 50, 50)
    pantalla.blit(imagen_volver, (x, y))
    
    return rect_volver

#--------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_reiniciar(pantalla) -> pygame.Rect:
    """
    Dibuja el boton reiniciar en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_reiniciar: Representa el area del boton reiniciar
    """
    
    x = 662
    y = 290
    ancho = 120
    alto = 40
    
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_reiniciar = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20)
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_reiniciar = fuente.render("Reiniciar", True, (0, 0, 0))
    pantalla.blit(texto_reiniciar, (x + 15, y + 5))
    
    return rect_reiniciar
#--------------------------------------------------------------------------------------------------------------
def dibujar_boton_pausa(pantalla) -> pygame.Rect:
    """
    Dibuja el boton pausa en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_pausa: Representa el area del boton pausa
    """
    x = 12
    y = 290
    ancho = 120
    alto = 40
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_pausa = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20) 
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_pausa = fuente.render("Pausa", True, (0, 0, 0))
    pantalla.blit(texto_pausa, (x + 28, y + 5))
    return rect_pausa

#--------------------------------------------------------------------------------------------------------------
def dibujar_errores(pantalla, cant_errores:int):
    """
    Dibuja el contador de errores en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el contador de errores
    """
    x = 495
    y = 28
    ancho = 120
    alto = 25


    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20)
    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    errores_texto_sombra = fuente.render("Errores:", True, (0, 0, 0))
    errores_texto = fuente.render("Errores:", True, (0, 0, 0))  
    pantalla.blit(errores_texto_sombra, (x + 6 , y + 1)) 
    pantalla.blit(errores_texto, (x + 5, y))
    errores_valor = fuente.render(f"{cant_errores}", True, (0, 0, 0))  
    pantalla.blit(errores_valor, (x + 80, y)) 

#--------------------------------------------------------------------------------------------------------------

def dibujar_tiempo(pantalla, tiempo_inicio) -> pygame.time:
    """
    Dibuja el tiempo en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el contador de errores
        tiempo_inicio: Representa el tiempo en el que inicia la partida
    """

    x = 170
    y = 28
    ancho = 120
    alto = 25


    tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000 
    minutos = tiempo_transcurrido // 60  # Minutos
    segundos = tiempo_transcurrido % 60  # Segundos restantes

    fuente = pygame.font.SysFont("Arial", 20, bold=True)
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20)
    tiempo_texto_sombra = fuente.render("Tiempo:", True, (0, 0, 0))
    tiempo_texto = fuente.render("Tiempo:", True, (0, 0, 0))  
    pantalla.blit(tiempo_texto_sombra, (x + 3 , y + 1))  
    pantalla.blit(tiempo_texto, (x + 2, y))  
    tiempo = fuente.render(f"{minutos:02}:{segundos:02}", True, (0, 0, 0)) 
    pantalla.blit(tiempo, (x + 75, y))  

    return tiempo

#--------------------------------------------------------------------------------------------------------------

def dibujar_boton_reanudar(pantalla) -> pygame.Rect:
    """
    Dibuja el boton reanudar en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_reanudar: Representa el area del boton reanudar
    """
    x = 300
    y = 400
    ancho = 120
    alto = 40
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2), border_radius= 20)
    rect_reanudar = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto), border_radius= 20) 
    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_reanudar = fuente.render("Reanudar", True, (0, 0, 0))
    pantalla.blit(texto_reanudar, (x + 20, y + 5))
    
    return rect_reanudar

def dibujar_boton_nueva_partida(pantalla) -> pygame.Rect:
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

def dibujar_boton_ver_puntajes(pantalla) -> pygame.Rect:
    """
    Dibuja el boton ver_puntajes en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja el boton
    
    Retorna:
        rect_ver_puntajes: Representa el area del boton reanuar
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



def dibujar_caja_texto(pantalla) -> pygame.Rect:
    """
    Dibuja la caja de texto en la pantalla

    Parametros:
        pantalla: Representa la pantalla donde se dibuja la caja de texto
    
    Retorna:
        rect_caja: Representa el area de la caja
    """
    x = 265
    y = 300
    ancho = 250
    alto = 40

    # Dibujar la caja
    pygame.draw.rect(pantalla, (0, 0, 0), (x - 2, y - 2, ancho + 2 * 2, alto + 2 * 2))
    rect_caja = pygame.draw.rect(pantalla, (200, 143, 90), (x, y, ancho, alto))

    return rect_caja

def ingresar_nombre(pantalla):
    """
    Permite ingresar el nombre del jugador en la caja de texto

    Parametros:
        pantalla: Representa la pantalla donde se escribe el nombre
    """
    nombre_jugador = ""
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.key == pygame.K_BACKSPACE: 
            nombre_jugador = nombre_jugador[0:-1] 
        elif evento.key == pygame.K_RETURN: 
            print("DEJO DE ESCRIBIR")
        else:
            nombre_jugador += evento.unicode 

    fuente = pygame.font.SysFont("Arial", 25, bold=True)
    texto_nombre = fuente.render(nombre_jugador, True, (0, 0, 0))
    pantalla.blit(texto_nombre, (270, 300))