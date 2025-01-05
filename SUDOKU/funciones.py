import random
import pygame
import copy
from constantes import *

def mostrar_matriz_sudoku(matriz: list) -> None:
    """
    Muestra la matriz de Sudoku con separaciones con pipes y guiones de submatrices cada 3 filas y columnas.

    Parametros:
        matriz (list): Matriz del Sudoku que se desea mostrar.

    Retorna:
        None: Esta funcion no retorna ningun valor.
    """
    for fila in range(len(matriz)):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)
        for columna in range(len(matriz[fila])):
            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")
            print(matriz[fila][columna], end=" ")
        print()

#---------------------------------------------------------------------------------------------------------------------------------

def mostrar_tablero_oculto(matriz: list, celdas_ocultas: list, caracter: str) -> None:
    """
    Muestra el tablero de Sudoku con ciertas celdas ocultas.
    
    Parámetros:
        matriz (list): Matriz de Sudoku.
        celdas_ocultas (list): Lista de posiciones (fila, columna) de las celdas ocultas.
        caracter (str): Caracter que se mostrara en las celdas ocultas.
    
    Retorna:
        None: Esta funcion no retorna ningun valor.
    """
    for fila in range(len(matriz)):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)
        for columna in range(len(matriz[fila])):
            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")

            if (fila, columna) in celdas_ocultas:
                print(caracter, end=" ")
            else:
                print(matriz[fila][columna], end=" ")
        print()

#---------------------------------------------------------------------------------------------------------------------------------

def inicializar_tablero_9x9(cantidad_filas: int = 9, cantidad_columnas: int = 9, valor_inicial: int = 0) -> list:
    """
    Inicializa una matriz de 9x9 con el valor inicial especificado.
    
    Parámetros:
        cantidad_filas (int): Cantidad de filas de la matriz (por defecto es 9).
        cantidad_columnas (int): Cantidad de columnas de la matriz (por defecto es 9).
        valor_inicial (int): Valor inicial para las celdas de la matriz (por defecto es 0).
    
    Retorna:
        matriz (list): Matriz de 9x9 inicializada con los valores especificados.
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_fila(matriz: list, numero: int, fila: int) -> bool:
    """
    Esta funcion verifica si un numero está repetido en la fila especificada de la matriz de Sudoku.
    
    Parametros:
        matriz (list): La matriz de Sudoku.
        numero (int): El numero que se desea verificar.
        fila (int): Indice de la fila donde se desea verificar.
    
    Retorna:
        resultado (bool): - Retorna True si el numero esta repetido en la fila
                        - False en caso contrario.
    """
    
    resultado = False
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == numero:
            resultado = True
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_columna(matriz: list, numero: int, columna: int) -> bool:
    """
    Esta funcion verifica si un numero esta repetido en la columna especificada de la matriz de Sudoku.
    
    Parámetros:
        matriz (list): La matriz de Sudoku.
        numero (int): El numero que se desea verificar.
        columna (int): Indice de la columna donde se desea verificar.
    
    Retorna:
        resultado: - True si el número está repetido en la columna
                - False en caso contrario.
    """
    
    resultado = False
    for fila in range(len(matriz)):
        if matriz[fila][columna] == numero:
            resultado = True
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------
def obtener_posicion_inicial_de_fila(fila:int) -> int:
    """
    Obtiene la posicion inicial de las filas en la matriz de Sudoku.
    
    Parametros:
        fila (int): Indice de las filas.
    
    Retorna:
        posicion_de_fila (int): Posicion inicial de las filas.
    """
    posicion_de_fila = 0
    if fila < 3:
        posicion_de_fila = 0
    elif fila < 6:
        posicion_de_fila = 3
    else:
        posicion_de_fila = 6
    return posicion_de_fila

#---------------------------------------------------------------------------------------------------------------------------------
def obtener_posicion_inicial_de_columna(columna:int) -> int:
    """
    Obtiene la posicion inicial de las columnas en la matriz de Sudoku.
    
    Parametros:
        fila (int): Indice de las columnas.
    
    Retorna:
        posicion_de_columna(int): Posicion inicial de las columnas.
    """
    posicion_de_columna = 0
    if columna < 3:
        posicion_de_columna = 0
    elif columna < 6:
        posicion_de_columna = 3
    else:
        posicion_de_columna = 6
    return posicion_de_columna

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_submatriz(matriz:list, numero:int, posicion_inicial_en_fila:int, posicion_inicial_en_columna:int) -> bool:
    """
    Esta funcion verifica si un numero esta repetido en la submatriz especificada de la matriz de Sudoku.
    
    Parametros:
        matriz (list): La matriz de Sudoku.
        numero (int): El numero que se desea verificar.
        posicion_inicial_en_fila (int): Indice de la fila donde se desea verificar.
        posicion_inicial_en_columna (int): Indice de la columna donde se desea verificar.
    
    Retorna:
    bandera_numero_repetido (bool): - True si el número esta repetido en la submatriz
                                    - False en caso contrario.
    """
    bandera_numero_repetido = False
    for indices_fila in range(posicion_inicial_en_fila, posicion_inicial_en_fila + 3):
        for indices_columna in range(posicion_inicial_en_columna, posicion_inicial_en_columna + 3):
            if matriz[indices_fila][indices_columna] == numero:
                bandera_numero_repetido = True
                break
        if bandera_numero_repetido == True:
            break
    return bandera_numero_repetido

#---------------------------------------------------------------------------------------------------------------------------------

def lista_posibles_numeros(desde: int = 1, hasta: int = 9) -> list:
    """
    Genera una lista de posibles enteros validos para ingresar en el sudoku (1-9).
    
    Parametros:
        desde (int): numero minimo (1).
        hasta (int): numero minimo (9).
    
    Retorna:
        posibles_numeros (list): Lista de enteros validos.
    """
    posibles_numeros = list(range(desde, hasta + 1))
    return posibles_numeros

#---------------------------------------------------------------------------------------------------------------------------------

def es_numero_valido(matriz: list, numero: int, fila: int, columna: int) -> bool:
    """
    Esta funcion verifica si un numero es valido para ingresar en la matriz de Sudoku.
    
    Parametros:
        matriz (list): La matriz de Sudoku.
        numero (int): El numero que se desea verificar.
        fila (int): Indice de la fila donde se desea verificar.
        columna (int): Indice de la columna donde se desea verificar.
    
    Retorna:
        numero_valido (bool): True si el número es valido
            - False en caso contrario.
    """
    numero_valido = False
    if (not verificar_numero_repetido_en_fila(matriz, numero, fila) and
        not verificar_numero_repetido_en_columna(matriz, numero, columna) and
        not verificar_numero_repetido_en_submatriz(matriz, numero, obtener_posicion_inicial_de_fila(fila), obtener_posicion_inicial_de_columna(columna))):
        matriz[fila][columna] = numero
        numero_valido = True
    return numero_valido

#---------------------------------------------------------------------------------------------------------------------------------

def resolver_sudoku(matriz: list, posibles_numeros: list, desde: int = 0, hasta: int = 9) -> bool:
    """
    Esta funcion toma la matriz 9x9 y resuelve el sudoku siguiendo las reglas tipicas.
    
    Parametros:
        matriz (list): La matriz de Sudoku.
        posibles_numeros (list): Lista de enteros validos.
        desde (int): El número inicial de fila o columna a recorrer (por defecto 0).
        hasta (int): El número final de fila o columna a recorrer (por defecto 9).
    
    Retorna:
        solucion_encontrada (bool): - True si la solucion fue encontrada (tablero resuelto)
                                    - False en caso contrario.
    """
    solucion_encontrada = True
    for fila in range(desde, hasta):
        for columna in range(desde, hasta):
            if matriz[fila][columna] == 0:
                solucion_encontrada = False
                random.shuffle(posibles_numeros)
                for numero in posibles_numeros:
                    if es_numero_valido(matriz, numero, fila, columna):
                        matriz[fila][columna] = numero
                        if resolver_sudoku(matriz, posibles_numeros, desde, hasta):
                            solucion_encontrada = True
                            break
                        matriz[fila][columna] = 0
                break
        if not solucion_encontrada:
            break
    return solucion_encontrada

#---------------------------------------------------------------------------------------------------------------------------------

def sudoku_celdas(cantidad_filas: int = 9, cantidad_columnas: int = 9) -> list:
    """
    Inicializa una matriz de 9x9 donde cada celda contiene su respectivo par ordenado (fila, columna).
    
    Parámetros:
        cantidad_filas (int): Cantidad de filas de la matriz (por defecto es 9).
        cantidad_columnas (int): Cantidad de columnas de la matriz (por defecto es 9).
    
    Retorna:
        matriz (list): Matriz de 9x9 con pares ordenados en cada celda.
    """
    matriz = [] 
    for fila in range(cantidad_filas):
        fila_celdas = []
        for columna in range(cantidad_columnas):
            fila_celdas.append((fila, columna))
        matriz.append(fila_celdas)
    return matriz


#---------------------------------------------------------------------------------------------------------------------------------

def generar_celdas(tamaño_del_tablero: int = 9) -> list:
    """
    Genera una lista de todas las posiciones del tablero.
    
    Parametros:
        tamaño_del_tablero (int): Tamaño del tablero (9x9).
        
    Retorna:
        celdas (list): Lista de tuplas con las posiciones del tablero.
    """
    celdas = []
    for fila in range(tamaño_del_tablero):
        for columna in range(tamaño_del_tablero):
            celdas.append((fila, columna))
    return celdas

#---------------------------------------------------------------------------------------------------------------------------------

def seleccionar_celdas_ocultas(celdas, celdas_a_ocultar):
    """
    Selecciona aleatoriamente las celdas que se van a ocultar.
    
    Parametros:
        celdas (list): Lista de celdas disponibles.
        celdas_a_ocultar (int): Número de celdas a ocultar.
        
    Retorna:
        celdas_a_ocultar (list): Lista de celdas seleccionadas para ocultar.
    """
    celdas_a_ocultar = random.sample(celdas, celdas_a_ocultar)
    return celdas_a_ocultar

#---------------------------------------------------------------------------------------------------------------------------------

def ocultar_datos_matriz_segun_dificultad(matriz: list, dificultad: str, total_celdas: int = 81, celdas_a_ocultar: int = 0) -> list:
    """
    Función para ocultar celdas aleatorias en el tablero según el nivel de dificultad.
    
    Parametros:
        matriz (list): Matriz del Sudoku (9x9) que se desea modificar.
        dificultad (str): Nivel de dificultad ("Facil", "Medio", "Dificil") segun desee el usuario.
        total_celdas (int): Cantidad de celdas del tablero
        celdas_a_ocultar (int): Cantidad de celdas a ocultar
        
    Retorna:
        matriz (list): Matriz modificada con celdas ocultas.
    """
    # Determinamos cuántas celdas ocultar según la dificultad
    if dificultad == "Facil":
        celdas_a_ocultar = int(total_celdas * 0.20)
    elif dificultad == "Medio":
        celdas_a_ocultar = int(total_celdas * 0.40)
    elif dificultad == "Dificil":
        celdas_a_ocultar = int(total_celdas * 0.60)
    
    celdas = generar_celdas()
    celdas_ocultas = seleccionar_celdas_ocultas(celdas, celdas_a_ocultar)

    for fila, columna in celdas_ocultas:
        matriz[fila][columna] = " "  # Valor de celda oculta
    return matriz

#---------------------------------------------------------------------------------------------------------------------------------
def dibujar_matriz_sudoku(pantalla, matriz, celda_actual, sudoku_terminado, desde: int = 0, hasta: int = 10):
    """
    Dibuja la matriz de Sudoku en la pantalla de Pygame.

    Parametros:
        pantalla: La pantalla de Pygame donde se dibujara.
        matriz: La matriz de Sudoku que se debe mostrar.
        celda_actual: La celda actual en la que se encuentra el usuario.
        sudoku_terminado: El sudoku del juego que debera completar el jugador
        desde, hasta: Conforman el rango para dibujar las lineas

    Retorna:
        rect_tablero : Retorna el rectangulo del tablero 
    """

    rect_tablero = pygame.Rect(INICIO_X, INICIO_Y, 9 * TAMAÑO_CELDA, 9 * TAMAÑO_CELDA)

    # Líneas horizontales y verticales
    for fila in range(desde, hasta): # hasta 10 asi dibuja la matriz correctamente.
        grosor = 3 if fila % 3 == 0 else 1  # Líneas más gruesas cada 3
        dibujar_linea(pantalla, COLOR_LINEA, fila, grosor, INICIO_X, INICIO_Y, TAMAÑO_CELDA)

    # Dibujar los números 
    fuente = pygame.font.SysFont("Arial", TAMAÑO_FUENTE)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if type(matriz[fila][columna]) == int:
                dibujar_numero(pantalla, fuente, matriz[fila][columna], fila, columna, INICIO_X, INICIO_Y, TAMAÑO_CELDA, COLOR_NUMEROS, celda_actual)
            else:
                if matriz[fila][columna] != " ":
                    if int(matriz[fila][columna]) != sudoku_terminado[fila][columna]:
                        dibujar_numero(pantalla, fuente, matriz[fila][columna], fila, columna, INICIO_X, INICIO_Y, TAMAÑO_CELDA, COLOR_ROJO, celda_actual)
                    else:
                        dibujar_numero(pantalla, fuente, matriz[fila][columna], fila, columna, INICIO_X, INICIO_Y, TAMAÑO_CELDA, COLOR_AZUL, celda_actual)
                else:
                    dibujar_numero(pantalla, fuente, matriz[fila][columna], fila, columna, INICIO_X, INICIO_Y, TAMAÑO_CELDA, COLOR_NUMEROS, celda_actual) # Sin esto no deaja resaltar celdas vacias
    return rect_tablero

#------------------------------------------------------------------------------------------

def dibujar_linea(pantalla, COLOR_LINEA, fila, grosor, INICIO_X, INICIO_Y, tamaño_celda):
    pygame.draw.line(pantalla, COLOR_LINEA, (INICIO_X, INICIO_Y + fila * tamaño_celda), (INICIO_X + COLUMNAS_DE_LA_MATRIZ * tamaño_celda, INICIO_Y + fila * tamaño_celda), grosor)
    pygame.draw.line(pantalla, COLOR_LINEA, (INICIO_X + fila * tamaño_celda, INICIO_Y), (INICIO_X + fila * tamaño_celda, INICIO_Y + FILAS_DE_LA_MATRIZ * tamaño_celda), grosor)

#------------------------------------------------------------------------------------------

def dibujar_numero(pantalla, fuente, numero, fila, columna, INICIO_X, INICIO_Y, TAMAÑO_CELDA, COLOR_NUMEROS, celda_actual):
    numeros = fuente.render(str(numero), True, COLOR_NUMEROS)
    x = INICIO_X + columna * TAMAÑO_CELDA + TAMAÑO_CELDA // 3
    y = INICIO_Y + fila * TAMAÑO_CELDA + TAMAÑO_CELDA // 4

    # Si la celda es la seleccionada, la resaltamos en blanco
    if celda_actual == (fila, columna):
        pygame.draw.rect(pantalla, COLOR_BLANCO, (INICIO_X + columna * TAMAÑO_CELDA, INICIO_Y + fila * TAMAÑO_CELDA, TAMAÑO_CELDA, TAMAÑO_CELDA))
    pantalla.blit(numeros, (x, y))


#------------------------------------------------------------------------------------------

def resaltar_celda(pantalla, celda_actual, sudoku_celdas):
    """
    Dibuja el Sudoku y resalta la celda seleccionada o donde está el mouse.

    Parámetros:
        pantalla: La pantalla de Pygame donde se dibujará.
        celda_actual: La celda actualmente seleccionada por el usuario (par ordenado de coordenadas).
        sudoku_celdas: Matriz de posiciones generada por la función sudoku_celdas.

    Retorna:
        celda_actual: La celda actual en la que se encuentra el usuario (o None si no se selecciona ninguna).
    """
    # Dimensiones del tablero basadas en las constantes
    rect_tablero = pygame.Rect(INICIO_X, INICIO_Y, FILAS_DE_LA_MATRIZ * TAMAÑO_CELDA, COLUMNAS_DE_LA_MATRIZ * TAMAÑO_CELDA)

    # Recorrer cada posición en la matriz generada por sudoku_celdas
    for fila_celdas in sudoku_celdas:
        for fila, columna in fila_celdas:
            # Calcular el rectángulo de la celda
            rect_celda = pygame.Rect(INICIO_X + columna * TAMAÑO_CELDA, INICIO_Y + fila * TAMAÑO_CELDA, TAMAÑO_CELDA, TAMAÑO_CELDA)
            
            # Detectar si el mouse está dentro de la celda
            if rect_celda.collidepoint(pygame.mouse.get_pos()):
                celda_actual = (fila, columna)
                pygame.draw.rect(pantalla, COLOR_BLANCO, rect_celda, GROSOR_DEL_BORDE)
                print(f"Celda actual: ({fila}, {columna})")
            
            # Si el mouse está fuera del tablero
            elif not rect_tablero.collidepoint(pygame.mouse.get_pos()):
                celda_actual = None

    return celda_actual


#--------------------------------------------------------------------------------------------

def matriz_resolucion() -> list:
    """
    Genera una matriz de Sudoku resuelta y la devuelve en su totalidad.
    
    Retorna:
        tablero (list): La matriz de Sudoku resuelto.
    """
    tablero = inicializar_tablero_9x9()
    posibles_numeros = lista_posibles_numeros()
    resolver_sudoku(tablero, posibles_numeros)
    mostrar_matriz_sudoku(tablero)
    print("\n")
    return tablero

#--------------------------------------------------------------------------------------------

def matriz_oculta(tablero_resuelto: list, dificultad: str) -> list:
    """
    Genera una copia de la matriz resuelta y oculta celdas según la dificultad especificada.
    
    Parámetros:
        tablero_resuelto (list): La matriz de Sudoku resuelta.
        dificultad (str): La dificultad del juego ('Facil', 'Medio', 'Dificil').
    
    Retorna:
        tablero_oculto (list): La copia de la matriz resuelta con celdas ocultas.
    """
    # Crear una copia de la matriz resuelta para trabajar sobre ella
    tablero_oculto = copy.deepcopy(tablero_resuelto)
    
    # Llamar a la función que oculta celdas según la dificultad
    ocultar_datos_matriz_segun_dificultad(tablero_oculto, dificultad)
    mostrar_matriz_sudoku(tablero_oculto)
    
    return tablero_oculto

#--------------------------------------------------------------------------------------------

def sudoku_modificable(sudoku_oculto):
    """
    Genera una copia de la matriz oculta para poder editarla sin afectar a la original.

    Parámetros:
        sudoku_oculto (list): La matriz de Sudoku oculta.
    
    Retorna:
        sudoku_actual (list): La copia de la matriz resuelta.
    """
    sudoku_actual = []
    for fila in sudoku_oculto:
        nueva_fila = [] 
        for valor in fila:
            nueva_fila.append(valor)
        sudoku_actual.append(nueva_fila)
    return sudoku_actual

#--------------------------------------------------------------------------------------------

def ingresar_numeros(tecla_presionada, sudoku_actual, sudoku_completo, celda_actual, cant_errores):
    if celda_actual is not None:
        fila, columna = celda_actual

        # Verificar que la celda esté vacía antes de permitir modificaciones
        if sudoku_actual[fila][columna] == ' ' or type(sudoku_actual[fila][columna]) == str:
            # Validar si la tecla es un número entre '1' y '9'
            if tecla_presionada.isdigit() and 1 <= int(tecla_presionada) <= 9:
                # Guardar el número ingresado en la celda seleccionada
                sudoku_actual[fila][columna] = str(tecla_presionada)
                print(sudoku_actual)
                celda_actual = None
                
                # Comparar con la matriz resuelta
                if int(tecla_presionada) != sudoku_completo[fila][columna]:
                    cant_errores += 1
                    celda_actual = None
                    print(f"Valor ingresado: {tecla_presionada}, Valor correcto: {sudoku_completo[fila][columna]}")

        # Manejar la tecla "backspace" para borrar la selección
        elif tecla_presionada == "backspace":
            celda_actual = None
        
        # Manejar la tecla "escape" para cancelar la selección
        elif tecla_presionada == "escape":
            celda_actual = None

    return sudoku_actual, celda_actual, cant_errores

#--------------------------------------------------------------------------------------------

def obtener_color_del_numero(matriz_original, matriz_modificable, tecla_ingresada, fila, columna, COLOR_CORRECTO, COLOR_INCORRECTO):
    """
    Determina el color que debe tener un número según si es correcto o incorrecto.
    
    Parámetros:
        matriz_original (list): La matriz de Sudoku original, con la solución.
        matriz_modificable (list): La matriz de Sudoku que el usuario está editando.
        fila (int): La fila de la celda.
        columna (int): La columna de la celda.
    
    Retorna:
        color (tuple): El color a usar (Rojo para incorrecto, Azul para correcto, None para no mostrar el color).
    """
    # Solo pintamos si el número es modificable (distinto de 0 en la matriz modificable)
    if str(tecla_ingresada) and matriz_modificable[fila][columna] != 0:
        if matriz_modificable[fila][columna] == matriz_original[fila][columna]:
            color_del_numero = COLOR_CORRECTO
        else:
            color_del_numero = COLOR_INCORRECTO
    return color_del_numero

#--------------------------------------------------------------------------------------------

def ganaste_el_sudoku(sudoku_actual, sudoku_completo) -> bool:
    """
    Determina si el sudoku se completo correctamente o no
    
    Parámetros:
       sudoku_actual: Representa el sudoku con el que interactua el jugador
       sudoku_completo: Representa el sudoku completo contra el que comparar si el sudoku_actual es igual
    
    Retorna:
       sudoku_actual_str == sudoku_completo_str (bool)
    """
    # Convertir ambos tableros a listas de cadenas
    sudoku_completo_str = []
    for fila in sudoku_completo:
        fila_str = [str(celda) for celda in fila]
        sudoku_completo_str.append(fila_str)

    sudoku_actual_str = []
    for fila in sudoku_actual:
        fila_str = [str(celda) for celda in fila]
        sudoku_actual_str.append(fila_str)

    return sudoku_actual_str == sudoku_completo_str

#--------------------------------------------------------------------------------------------

def calcular_puntaje(cant_errores, minutos, dificultad, puntaje_base, bonus_dificultad):
    """
    Calcula el puntaje obtenido por el jugador
    
    Parámetros:
       cant_errores: Representa la cantidad de errores cometidos
       minutos: Representa los minutos transcurridos por los que se penalizaran puntos
       dificultad: Representa la dificultad del juego
       puntaje_base: Representa la cantidad de puntos con la que se inicia el juego
       bonus_dificutad: Representa un bonus segun la dificultad del juego
    
    Retorna:
       puntaje_final (float): Representa el puntaje final obtenido
    """
    if dificultad == "Facil":
        bonus_dificultad = 1.25
    elif dificultad == "Medio":
        bonus_dificultad = 1.5
    elif dificultad == "Dificil":
        bonus_dificultad = 1.75    

    # Calcular el puntaje final restando puntos por los errores y el tiempo, multiplicado por el bono de dificultad
    puntaje_final = (puntaje_base - (cant_errores * 50) - (minutos * 10)) * bonus_dificultad
    if puntaje_final < 0:
        puntaje_final = 0
    return puntaje_final


def calcular_tiempo(tiempo_inicio):
    tiempo_transcurrido = pygame.time.get_ticks() - tiempo_inicio
    # Minutos
    minutos_transcurridos = tiempo_transcurrido // 60000

    return minutos_transcurridos

def ordenar_puntajes(lista_puntajes: list):
    """
    Ordena los puntaje de la lista_puntajes del más alto al más bajo

    Parámetros:
       lista_puntajes: Representa la lista que contiene los datos de los puntajes obtenidos por los jugadores
    """
    for i in range(len(lista_puntajes) -1):
        for j in range(i+1,len(lista_puntajes)):
            if lista_puntajes[i]["puntos"] < lista_puntajes[j]["puntos"]:
                aux_puntaje = lista_puntajes[i]
                lista_puntajes[i] = lista_puntajes[j]
                lista_puntajes[j] = aux_puntaje
            
def buscar_jugador(lista_puntajes: list, nombre_jugador: str) -> int:
    """
    Busca si un jugador se encuentra o no en la lista de puntajes

    Parámetros:
       lista_puntajes: Representa la lista que contiene los datos de los puntajes obtenidos por los jugadores
       nombre_jugador: Representa el nombre del jugador a buscar

    Retorna:
        indice (int): Representa en indice de la lista en el que se encuentra al jugador
    """
    indice = None
    
    for i in range(len(lista_puntajes)):
        if lista_puntajes[i]["nombre"] == nombre_jugador:
            indice = i
            break
    
    return indice

def cambiar_estadisticas_jugador(lista_puntajes: list, indice_jugador: int, puntos: float, nombre: str):
    """
    Modifica los datos de un jugador para que solo se guarde su puntaje más alto en la lista_puntajes

    Parámetros:
       lista_puntajes: Representa la lista que contiene los datos de los puntajes obtenidos por los jugadores
       indice_jugador: Representa en indice de la lista en el que se encuentra al jugador
       puntos: Representa la cantidad de puntos del jugador
       nombre: Representa el nombre del jugador
    """
    if indice_jugador != None:
        if puntos > lista_puntajes[indice_jugador]["puntos"]:
            lista_puntajes[indice_jugador]["puntos"] = puntos
    else:
        diccionario_jugador = {}
        diccionario_jugador["nombre"] = nombre
        diccionario_jugador["puntos"] = puntos
        lista_puntajes.append(diccionario_jugador)