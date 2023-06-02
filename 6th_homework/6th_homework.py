# Funciones en Python
# Due May 26, 2023 11:59 PM
# Instructions:
# Calculadora de área y perímetro

# Crear un programa en Python que utilice funciones para calcular
# el área y el perímetro de diferentes figuras geométricas. El programa
# debe ofrecer al usuario un menú de opciones para que pueda seleccionar
# la figura con la que desea trabajar: cuadrado, triángulo o círculo. 
# Una vez seleccionada la figura, el programa debe solicitar los datos 
# necesarios al usuario para realizar los cálculos. 

# El programa debe tener una función para cada figura geométrica que 
# calcule y retorne el área y el perímetro correspondientes. Una vez
# realizados los cálculos, el programa debe mostrar los resultados al 
# usuario de forma clara y legible, indicando el valor del área y el 
# perímetro de la figura seleccionada.

# Utilizar nombres descriptivos para las funciones y comentarios (docstrings)
# para explicar el propósito de cada una. Además, considera manejar correctamente
# los tipos de datos y posibles errores de entrada por parte del usuario.

import math
import os

    # la librería "math" se utiliza para acceder a la constante matemática 
    # "pi" (math.pi) y para calcular la raíz cuadrada (math.sqrt()). Estas
    # funciones son utilizadas para calcular el área y el perímetro del círculo.

# función para imprimir encabezados centrados
def print_header(text):

    # La función get_terminal_size() devuelve un objeto 
    # os.terminal_size que contiene el tamaño actual de la terminal.
    terminal_size = os.get_terminal_size().columns
    header = text.center(terminal_size)
    print(header)

def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado.
    :param lado: Longitud del lado del cuadrado.
    :return: Área del cuadrado.
    """
    area = lado ** 2
    return area

def calcular_perimetro_cuadrado(lado):
    """
    Calcula el perímetro de un cuadrado.
    :param lado: Longitud del lado del cuadrado.
    :return: Perímetro del cuadrado.
    """
    perimetro = lado * 4
    return perimetro

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    :param base: Base del triángulo.
    :param altura: Altura del triángulo.
    :return: Área del triángulo.
    """
    area = (base * altura) / 2
    return area

def calcular_perimetro_triangulo(base, altura):
    """
    Calcula el perímetro de un triángulo (solo en base a base y altura).
    :param base: Base del triángulo.
    :param altura: Altura del triángulo.
    :return: Perímetro del triángulo.
    """
    lado = math.sqrt((base / 2) ** 2 + altura ** 2)
    perimetro = base + (2 * lado)
    return perimetro

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.
    :param radio: Radio del círculo.
    :return: Área del círculo.
    """
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro de un círculo.
    :param radio: Radio del círculo.
    :return: Perímetro del círculo.
    """
    perimetro = 2 * math.pi * radio
    return perimetro

def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("--------------------------------------")
    print("|| Seleccione la figura geométrica: ||")
    print("--------------------------------------")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Círculo")
    print("4. Salir\n")

def obtener_numero(mensaje):
    """
    Solicita al usuario un número y lo devuelve.
    :param mensaje: El mensaje a mostrar al usuario.
    :return: El número ingresado por el usuario.
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    while True:
        mostrar_menu()
        opción = obtener_numero("Ingrese el número de la figura deseada: ")

        if opción == 1:
            lado = obtener_numero("\nIngrese la longitud del lado del cuadrado: ")
            area = calcular_area_cuadrado(lado)
            perimetro = calcular_perimetro_cuadrado(lado)
            print(f"\nEl área del cuadrado es: {area}")
            print(f"El perímetro del cuadrado es: {perimetro}\n")
        elif opción == 2:
            base = obtener_numero("\nIngrese la base del triángulo: ")
            altura = obtener_numero("Ingrese la altura del triángulo: ")
            area = calcular_area_triangulo(base, altura)
            perimetro = calcular_perimetro_triangulo(base, altura)
            print(f"\nEl área del triángulo es: {area}")
            print(f"El perímetro del triángulo es: {perimetro}\n")
        elif opción == 3:
            radio = obtener_numero("\nIngrese el radio del círculo: ")
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            print(f"\nEl área del círculo es: {area}")
            print(f"El perímetro del círculo es: {perimetro}\n")
        elif opción == 4:
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

## Imprimir encabezados
print_header("UNIVERSIDAD PANAMERICANA DE GUATEMALA")
print_header("Campus de Cobán Alta Verapaz")
print_header("Facultad de Ingeniería y Ciencias Aplicadas")
print_header("Carrera de Ingeniería en Sistemas y Tecnologías de la Información y Comunicación")
print_header("Abel Fernando Avendaño Argueta 000127599")

## Ejecución del programa

# Saludo
print("\n\n         Bienvenido a este programa! \n\n")

if __name__ == "__main__":
    main()