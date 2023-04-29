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
    global x_Function
    global y_Function

    x_Function = float(input("\nIngrese el valor de x: "))

    y_Function1 = (a)*(x_Function**2) + (b*x_Function) + c
    x_Function = round(x_Function)
    y_Function1 = round(y_Function1)
    coordenada_Function = (x_Function, (y_Function1))
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

coordenadas = {}
newKeys_coord = {}
patron_CartesianPlane = {}

# Entradas de usuario en relación a, b y c que no deberían cambiar a lo
# largo de la ejecución del script

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Otras variables globales necesarias

x_Function = 0
y_Function = 0

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

## Generación de plano cartesiano

# Generación de filas/lineas de plano cartesiano
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

imprimir_plano_cartesiano(patron_CartesianPlane)

print("\n character just for debugging: \n")
print(patron_CartesianPlane[100][50])

print("\n coor just for debugging: \n")

print(newKeys_coord[46][53])

# Impresión de valor de coordenada
coordenada_Solved = calcular_coordenada()
print("\n La coordenada correspondiente es: \n", coordenada_Solved)

position_CoorInDict = buscar_coordenada(newKeys_coord, coordenada_Solved)

print("\n La posicion a la previa coor en el diccionario es: \n")
print(position_CoorInDict)

patron_CartesianPlane = sustituir_caracter(position_CoorInDict, patron_CartesianPlane)
