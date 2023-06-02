# Funciones Lambda en Python
# Due tomorrow at 11:59 PM
# Instructions
# Calculadora de área y perímetro

# Crear un programa en Python que utilice funciones lambda para
# calcular el área y el perímetro de diferentes figuras geométricas.
# El programa debe ofrecer al usuario un menú de opciones para que
# pueda seleccionar la figura con la que desea trabajar: cuadrado,
# triángulo o círculo. Una vez seleccionada la figura, el programa
# debe solicitar los datos necesarios al usuario para realizar los
# cálculos. 

# El programa debe tener una funciones lambda para cada figura 
# geométrica que calcule y retorne el área y el perímetro 
# correspondientes. Una vez realizados los cálculos, el programa debe
# mostrar los resultados al usuario de forma clara y legible, indicando
# el valor del área y el perímetro de la figura seleccionada.

# Utilizar nombres descriptivos para las variables. Además, considera 
# manejar correctamente los tipos de datos y posibles errores de 
# entrada por parte del usuario.

import os
import math

    # la librería "math" se utiliza para acceder a la constante matemática 
    # "pi" (math.pi) y para calcular la raíz cuadrada (math.sqrt()). Estas
    # funciones son utilizadas para calcular el área y el perímetro del círculo.
    # Definición de funciones lambda para calcular el área y perímetro de cada figura

area_perimetro_cuadrado = lambda lado: (lado ** 2, lado * 4)
area_perimetro_triangulo = lambda base, altura: (base * altura / 2, base + (2 * (math.sqrt((base / 2) ** 2 + altura ** 2))))
area_perimetro_circulo = lambda radio: (math.pi * radio ** 2, 2 * math.pi * radio)


# función para imprimir encabezados centrados

def print_header(text):

    # La función get_terminal_size() devuelve un objeto 
    # os.terminal_size que contiene el tamaño actual de la terminal.
    terminal_size = os.get_terminal_size().columns
    header = text.center(terminal_size)
    print(header)


# Función para mostrar el menú y realizar los cálculos

def calcular_figura():
    while True:
        print("--------------------------------------")
        print("|| Seleccione la figura geométrica: ||")
        print("--------------------------------------")
        print("1. Cuadrado")
        print("2. Triángulo")
        print("3. Círculo")
        print("4. Salir\n")

        figura = input("Ingrese el número de la figura: ")
        print() # Salto de linea

        if figura == "1":
            lado = float(input("Ingrese la longitud del lado del cuadrado: "))
            area, perimetro = area_perimetro_cuadrado(lado)
            print(f"\nEl área del cuadrado es: {area}")
            print(f"El perímetro del cuadrado es: {perimetro}\n")
        elif figura == "2":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area, perimetro = area_perimetro_triangulo(base, altura)
            print(f"\nEl área del triángulo es: {area}")
            print(f"El perímetro del triángulo es: {perimetro}\n")
        elif figura == "3":
            radio = float(input("Ingrese el radio del círculo: "))
            area, perimetro = area_perimetro_circulo(radio)
            print(f"\nEl área del círculo es: {area}")
            print(f"El perímetro del círculo es: {perimetro}\n")
        elif figura == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una figura válida.\n")

## Imprimir encabezados
print_header("UNIVERSIDAD PANAMERICANA DE GUATEMALA")
print_header("Campus de Cobán Alta Verapaz")
print_header("Facultad de Ingeniería y Ciencias Aplicadas")
print_header("Carrera de Ingeniería en Sistemas y Tecnologías de la Información y Comunicación")
print_header("Abel Fernando Avendaño Argueta 000127599")

## Ejecución del programa

# Saludo
print("\n\n         Bienvenido a este programa! \n\n")

# Ejecución del programa
calcular_figura()