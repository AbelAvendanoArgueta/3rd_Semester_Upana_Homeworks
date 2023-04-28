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

def crear_tablero():
    # Define el tamaño del tablero
    altura = 100
    ancho = 100

    # Crea una matriz vacía del tamaño del tablero
    tablero = [[" " for _ in range(ancho)] for _ in range(altura)]

    # Dibuja los ejes x e y
    for i in range(ancho):
        tablero[altura//2][i] = "-"
    for i in range(altura):
        tablero[i][ancho//2] = "|"

    # Dibuja los cuadrantes
    for i in range(ancho):
        for j in range(altura):
            if i == ancho//2 and j == altura//2:
                tablero[j][i] = "0"
            elif i == ancho//2:
                tablero[j][i] = "|"
            elif j == altura//2:
                tablero[j][i] = "-"
            elif i > ancho//2 and j < altura//2:
                tablero[j][i] = "."
            elif i < ancho//2 and j < altura//2:
                tablero[j][i] = "."
            elif i < ancho//2 and j > altura//2:
                tablero[j][i] = "."
            elif i > ancho//2 and j > altura//2:
                tablero[j][i] = "."

    # Crea un diccionario con las filas del tablero
    diccionario_tablero = {i: "".join(fila) + "\n" for i, fila in enumerate(tablero)}

    return tablero, diccionario_tablero

# Llama a la función y guarda los valores devueltos en variables
tablero, diccionario_tablero = crear_tablero()

# Imprime el tablero
for fila in tablero:
    print("".join(fila))

print("\n separación \n")

# Imprime el diccionario
print("".join(diccionario_tablero.values()))
