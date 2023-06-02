import math

# Definición de funciones lambda para calcular el área y perímetro de cada figura

area_perimetro_cuadrado = lambda lado: (lado ** 2, lado * 4)
area_perimetro_triangulo = lambda base, altura: (base * altura / 2, base + (2 * (math.sqrt((base / 2) ** 2 + altura ** 2))))
area_perimetro_circulo = lambda radio: (math.pi * radio ** 2, 2 * math.pi * radio)
 
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

# Ejecución del programa
calcular_figura()