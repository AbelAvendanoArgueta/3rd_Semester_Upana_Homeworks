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