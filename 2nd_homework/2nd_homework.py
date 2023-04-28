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
print("\n\n         Bienvenido a este pograma! \n\n")

# variables fueron declaradas como float en caso que el
# usuario decida ingresar un valor decimal o no entero
var1 = float(input("Ingrese el primer número: "))
var2 = float(input("Ingrese el segundo número: "))

# Suma
suma = var1 + var2
print("La suma es:", suma)

# Resta
resta = var1 - var2
print("La resta es:", resta)

# Multiplicación
multiplicacion = var1 * var2
print("La multiplicación es:", multiplicacion)

# División entera
division_entera = var1 // var2
print("La división entera es:", division_entera)

# Residuo
residuo = var1 % var2
print("El residuo es:", residuo)

# División con decimales
division_decimal = var1 / var2
print("La división con decimales es: {:.2f}".format(division_decimal))

# Exponencial
exponencial = var1 ** var2
print("La exponencial es:", exponencial)