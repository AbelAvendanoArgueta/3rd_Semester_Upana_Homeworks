"""
Ciclo While
Due tomorrow at 11:59 PM

Instructions:

Crear un programa en Python que permita graficar cualquier ecuación cuadrática utilizando el método de ploteo. El programa debe cumplir las siguientes características:

    - Iniciar con un saludo al usuario. 
    - Solicitar al usuario el ingreso de los siguientes parámetros:
        * El valor de "a": Coeficiente que acompaña a la literal cuadrática
        * El valor de "b": Coeficiente que acompaña a la literal con exponente 1.
        * El valor de "c": Coeficiente que no tiene literal.
    - Plotear la gráfica en la consola de Python en una matriz cuadrada de 100 espacios por 100 líneas.
"""
"""
Notas del estudiante a tomar en cuenta:

    Una función bastante probada es la siguiente: "f(x) = 1x^2 - 2x + 1"
    donde el programa puede graficar puntos desde -6, -5, -4... hasta 8

    Funciones que grafiquen puntos mas haya de (-50,50) y (50,-50) en términos
    de "X" y "Y" no podrán ser graficados usando este script, en tal caso
    le invitaria a usar  5th_homework_0.2.py

"""

# Librerías Importantes
import os

# función para imprimir encabezados centrados
def print_header(text):

    # La función get_terminal_size() devuelve un objeto 
    # os.terminal_size que contiene el tamaño actual de la terminal.
    terminal_size = os.get_terminal_size().columns
    header = text.center(terminal_size)
    print(header)

## Imprimir encabezados
print_header("UNIVERSIDAD PANAMERICANA DE GUATEMALA")
print_header("Campus de Cobán Alta Verapaz")
print_header("Facultad de Ingeniería y Ciencias Aplicadas")
print_header("Carrera de Ingeniería en Sistemas y Tecnologías de la Información y Comunicación")
print_header("Abel Fernando Avendaño Argueta 000127599")


## Ejecución del programa

# Saludo
print("\n\n         Bienvenido a este programa! \n\n")

def calcular_coordenada():
    # función para solicitar el valor de x
    # en distintos momentos del programa, para ir graficando

    global a
    global b
    global c
    x_Function = 0
    y_Function = 0

    # El valor de x se solicita distintas veces para 
    # trazar diferentes puntos en la gráfica
    x_Function = float(input("\nIngrese el valor de x: "))

    # Aquí aplico mate que debí aprender desde segundo básico
    y_Function = (a)*(x_Function**2) + (b*x_Function) + c

    # Ni modo, vamos a graficar en consola no?
    # asi que le vamos a aproximar, ya si queremos puntos mas exactos
    # le invito a usar  5th_homework_0.2.py
    x_Function = round(x_Function)
    y_Function = round(y_Function)
    coordenada_Function = (x_Function, (y_Function))

    return coordenada_Function

def buscar_coordenada(diccionario, coordenada):
    # función para buscar posición de la coordenada dentro del
    # diccionario newKeys_coord = {}
    for i, lista_coordenadas in diccionario.items():
        if coordenada in lista_coordenadas:
            return i, lista_coordenadas.index(coordenada)
    return None

def actualizar_patron(coordenada, diccionario):
    pos = buscar_coordenada(diccionario, coordenada)
    if pos is not None:
        fila, columna = pos
        diccionario[fila][columna] = "*"

def sustituir_caracter(position_CoorInDict, patron_CartesianPlane):
    # Extraemos el índice de fila y columna del diccionario a partir de position_CoorInDict
    i, j = position_CoorInDict

    # Sustituimos el caracter en la posición correspondiente por el símbolo "*"
    patron_CartesianPlane[i][j] = "*"

    # Imprimimos el plano cartesiano actualizado
    imprimir_plano_cartesiano(patron_CartesianPlane)

    return patron_CartesianPlane

def imprimir_plano_cartesiano(plano_cartesiano):
    # Función para imprimir plano cartesiano
    for fila in plano_cartesiano.values():
        for caracter in fila:
            print(caracter, end="")
        print()

def generacion_coordenadas():
    global coordenadas
    global newKeys_coord
    # Generación de coordenadas
    for y in range(50, -51, -1):
        coordenadas[y] = []
        for x in range(-50, 51):
            coordenadas[y].append((x, y))

    # Ordenamiento de claves en el diccionario de 
    # coordenadas para que hagan match con los puntos
    # del plano cartesiano
    i = 0
    for y in range(50, -51, -1):
        newKeys_coord[i] = []
        for x in range(-50, 51):
            newKeys_coord[i].append((x, y))
        i += 1
    return coordenadas, newKeys_coord

def generacion_plano_cartesiano():
    ## Generación de plano cartesiano
    for j in range(101):
        if j == 50:
            patron_CartesianPlane[j] = ["-" for i in range(101)]
        else:
            linea = []
            for i in range(50):
                linea.append(".")
            linea.append("|")
            for i in range(50):
                linea.append(".")
            patron_CartesianPlane[j] = linea
    return patron_CartesianPlane
    
# Listas globales
coordenadas = {}
newKeys_coord = {}
patron_CartesianPlane = {}

# Entradas de usuario en relación a, b y c que no deberían cambiar a lo
# largo de la ejecución del script

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

generacion_coordenadas()
generacion_plano_cartesiano()

while True:
    # Impresión de valor de coordenada
    coordenada_Solved = calcular_coordenada()

    position_CoorInDict = buscar_coordenada(newKeys_coord, coordenada_Solved)

    patron_CartesianPlane = sustituir_caracter(position_CoorInDict, patron_CartesianPlane)

    # Preguntamos al usuario si desea continuar graficando
    respuesta = input("\n¿Desea ingresar otro valor de 'X'? (sí/no): ")
    if respuesta.lower() == "no":
        break
