import math

    # la librería "math" se utiliza para acceder a la constante matemática 
    # "pi" (math.pi) y para calcular la raíz cuadrada (math.sqrt()). Estas
    # funciones son utilizadas para calcular el área y el perímetro del círculo.

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

if __name__ == "__main__":
    main()