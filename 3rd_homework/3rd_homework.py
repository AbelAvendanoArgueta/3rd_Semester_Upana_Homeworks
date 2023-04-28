"""
Sentencia IF y operadores de comparación en Python
Due March 17, 2023 11:59 PM
Closes April 14, 2023 11:59 PM

Instructions:

Crear un programa en Python, que cumpla con las siguientes funcionalidades: 
Imprimir mensaje de bienvenida al usuario.

    - Solicitar al usuario el ingreso de un número.
    - Comprobar si el numero ingresado es positivo o negativo, e imprimir la respuesta.
    - Comprobar si el numero ingresado es par o impar, e imprimir la respuesta. 
"""

# Librerias Importantes
import os

# funcion para imprimir encabezados centrados
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

# Se solicita entrada de usuario
numero = int(input("Por favor, ingrese un número: "))

# Se verifica si el numero es mayor o menor
if numero > 0:
    print("El número ingresado es positivo.")
elif numero < 0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es cero.")

# Se verifica si el numero es par
# Si hay resto no es par
if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")
