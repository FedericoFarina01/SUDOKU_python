import pygame
from funciones import *
from botones import *
from constantes import *
from archivos import *
from pantallas.inicio import dibujar_pantalla_inicio, cambiar_dificultad
from pantallas.principal import dibujar_pantalla_principal
from pantallas.puntajes import dibujar_pantalla_puntajes
from pantallas.pausa import dibujar_pantalla_pausa
from pantallas.ganaste import dibujar_pantalla_ganaste


#--------------------------------------------------------------------------------------------------------------
# Inicializamos pygame
pygame.init()
#--------------------------------------------------------------------------------------------------------------

# Configuración de la pantalla
pantalla = pygame.display.set_mode(DIMENSION_PANTALLA)

#--------------------------------------------------------------------------------------------------------------

# Crear pantalla
pantalla = pygame.display.set_mode(DIMENSION_PANTALLA)

#--------------------------------------------------------------------------------------------------------------

# Cambiar el título del juego
pygame.display.set_caption("Sudoku")

#--------------------------------------------------------------------------------------------------------------

# Icono del juego
img_icono = pygame.image.load("SUDOKU/imagenes/icon_sudoku.png")
pygame.display.set_icon(img_icono)

#--------------------------------------------------------------------------------------------------------------

# Música
pygame.mixer.init()
pygame.mixer.music.load("SUDOKU/musica/Vibe Mountain.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
#--------------------------------------------------------------------------------------------------------------

# Variables
juego_corriendo = True
pantalla_activa = "inicio"
nombre_jugador = ""
click_izq = pygame.MOUSEBUTTONDOWN
dificultad = "Facil"
cant_errores = 0
puntaje_base = 1000
caja_texto_activa = False

if dificultad == "Facil":
    bonus_dificultad = 1.25
elif dificultad == "Medio":
    bonus_dificultad = 1.5
elif dificultad == "Dificil":
    bonus_dificultad = 1.75  

#--------------------------------------------------------------------------------------------------------------

# Variables para el Sudoku
celda_actual = None
sudoku_completo = None
sudoku_oculto = None
sudoku_actual = None

#--------------------------------------------------------------------------------------------------------------

# Variables json
json_puntajes = "SUDOKU/usuarios.json"
user_text = nombre_jugador  # Inicializa con el nombre actual del jugador
input_rect = pygame.Rect(300, 300, 200, 40)
fuente_texto = pygame.font.SysFont("Arial", 30)
lista_puntajes = leer_json(json_puntajes)

#--------------------------------------------------------------------------------------------------------------

while juego_corriendo:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            juego_corriendo = False
            pygame.quit()
            quit()

        # Detectar clics del mouse
        if evento.type == click_izq:
            cursor = pygame.mouse.get_pos()

            # Detectar clic en los botones de la pantalla de inicio
            if pantalla_activa == "inicio":
                if dibujar_boton_jugar(pantalla).collidepoint(cursor):
                    # Cuando el jugador haga clic en "Jugar", generamos el Sudoku
                    tiempo_inicio = pygame.time.get_ticks()
                    pantalla_activa = "principal"
                    sudoku_completo = matriz_resolucion()
                    sudoku_oculto = matriz_oculta(sudoku_completo, dificultad)
                    sudoku_actual = sudoku_modificable(sudoku_oculto)
                    celda_actual = None
                    
                elif dibujar_boton_puntajes(pantalla).collidepoint(cursor): # PUNTAJES
                    ordenar_puntajes(lista_puntajes)
                    pantalla_activa = "puntajes"

                elif dibujar_boton_salir(pantalla).collidepoint(cursor): # SALIR
                    juego_corriendo = False
                    pygame.quit()
                    quit()

                elif dibujar_boton_dificultad(pantalla, dificultad).collidepoint(cursor): # DICULTAD
                    dificultad = cambiar_dificultad(dificultad)

            # Detectar clic en los botones de la pantalla principal
            elif pantalla_activa == "principal":
                celda_actual = resaltar_celda(pantalla, celda_actual, sudoku_celdas())

                if dibujar_boton_reiniciar(pantalla).collidepoint(cursor): # REINICIAR
                    celda_actual = None
                    sudoku_completo = matriz_resolucion()
                    sudoku_oculto = matriz_oculta(sudoku_completo, dificultad) 
                    sudoku_actual = sudoku_modificable(sudoku_oculto)
                    tiempo_inicio = pygame.time.get_ticks()
                    cant_errores = 0

                elif dibujar_boton_volver(pantalla).collidepoint(cursor): # VOLVER
                    celda_actual = None
                    pantalla_activa = "inicio"
                    pygame.mixer.music.play(-1)

                elif dibujar_boton_pausa(pantalla).collidepoint(cursor): # PAUSA
                    pantalla_activa = "pausa"
                    
            # Detectar clic en los botones de la pantalla pausa
            elif pantalla_activa == "pausa":
                if dibujar_boton_reanudar(pantalla).collidepoint(cursor): # REANUDAR
                        pantalla_activa = "principal"

            # Detectar clic en los botones de la pantalla ganaste
            elif pantalla_activa == "ganaste":
                if dibujar_boton_nueva_partida(pantalla).collidepoint(cursor):
                    pantalla_activa = "principal"
                    celda_actual = None
                    sudoku_completo = matriz_resolucion()
                    sudoku_oculto = matriz_oculta(sudoku_completo, dificultad) 
                    sudoku_actual = sudoku_modificable(sudoku_oculto)
                    tiempo_inicio = pygame.time.get_ticks()
                    cant_errores = 0

                elif dibujar_boton_ver_puntajes(pantalla).collidepoint(cursor):
                    pantalla_activa = "puntajes"

                elif pantalla_activa == "ganaste": # Seleccionar caja de texto
                    if dibujar_caja_texto(pantalla).collidepoint(cursor):
                        caja_texto_activa = True  
                    else:
                        caja_texto_activa = False 

            # Detectar clic en los botones de la pantalla puntajes
            elif pantalla_activa == "puntajes":
                if dibujar_boton_volver(pantalla).collidepoint(cursor):
                    pantalla_activa = "inicio"

        # Eventos de teclado
        if evento.type == pygame.KEYDOWN:
            tecla_presionada = pygame.key.name(evento.key)
            if pantalla_activa == "principal":
                sudoku_actual, celda_actual, cant_errores = ingresar_numeros(tecla_presionada, sudoku_actual, sudoku_completo, celda_actual, cant_errores)

                # Verificar si el Sudoku está completado
                if ganaste_el_sudoku(sudoku_actual, sudoku_completo):
                    pantalla_activa = "ganaste"  # Cambiar a la pantalla de 'ganaste'
                    tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000  # Tiempo en segundos
                    minutos = tiempo_transcurrido // 60
                    segundos = tiempo_transcurrido % 60
                    puntaje_final = calcular_puntaje(cant_errores, minutos, dificultad, puntaje_base, bonus_dificultad)
                    cant_errores = 0


                if tecla_presionada == "backspace":
                    celda_actual == " "

                if evento.key == pygame.K_DELETE:
                    fila, columna = celda_actual
                    if sudoku_actual[fila][columna] != " " and type(sudoku_actual[fila][columna]) == str:
                        sudoku_actual[fila][columna] = " "

                    rect_tablero = dibujar_matriz_sudoku(pantalla, sudoku_actual, celda_actual,sudoku_completo)

            # Escribir nombre en caja de texto
            elif pantalla_activa == "ganaste" and caja_texto_activa: 
                if evento.key == pygame.K_BACKSPACE:
                    nombre_jugador = nombre_jugador[:-1]  
                elif len(nombre_jugador) < 15 and evento.key != pygame.K_RETURN:  
                    nombre_jugador += evento.unicode

                elif evento.key == pygame.K_RETURN:
                    if 0 < len(nombre_jugador) <= 15:
                        indice_jugador = buscar_jugador(lista_puntajes,nombre_jugador)
                        cambiar_estadisticas_jugador(lista_puntajes,indice_jugador,puntaje_final,nombre_jugador)
                        guardar_json(json_puntajes, lista_puntajes)
                        pantalla_activa = "inicio"
                        nombre_jugador = ""
                    else:
                        caja_texto_activa = False



    # Dibujar pantallas
    if pantalla_activa == "inicio":
        dibujar_pantalla_inicio(pantalla, dificultad)

    elif pantalla_activa == "puntajes":
        dibujar_pantalla_puntajes(pantalla,lista_puntajes)

    elif pantalla_activa == "principal":
        dibujar_pantalla_principal(pantalla, tiempo_inicio, cant_errores)
        rectangulo_sudoku = dibujar_matriz_sudoku(pantalla, sudoku_actual, celda_actual,sudoku_completo)
        boton_pausa = dibujar_boton_pausa(pantalla)

    elif pantalla_activa == "pausa":
        dibujar_pantalla_pausa(pantalla, ANCHO_PANTALLA, LARGO_PANTALLA)

    elif pantalla_activa == "ganaste":
        # Dibujar pantalla de ganaste con el puntaje calculado
        dibujar_pantalla_ganaste(pantalla, puntaje_final, nombre_jugador)

    pygame.display.flip()