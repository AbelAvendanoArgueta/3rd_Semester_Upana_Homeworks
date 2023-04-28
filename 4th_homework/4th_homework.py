"""
Listas, tuplas y diccionarios en Python
Due March 31, 2023 11:59 PM
Closes April 14, 2023 11:59 PM

Instructions:

Crear un programa que cumpla con las siguientes funcionalidades:

    - Iniciar con un saludo al usuario.
    - Solicitar al usuario el ingreso de: Nombre, Apellido, Edad, Genero, Documento de identidad, profesión, estado civil. 
    - Los datos ingresados se deben almacenar en una variable de tipo lista para su posterior manipulación.
    - A partir de la información proporcionada por el usuario mostrar: año de nacimiento, lugar de nacimiento, y consultar al usuario si desea modificar alguno de los datos.
"""

from unidecode import unidecode
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



print_header("Por favor completar los siguientes datos: \n\n")

# New list / creacion de nueva lista

personal_data = []

## User inputs / Entradas de usuario

# name [0]
personal_data.append(str(input("Ingresa tus nombres: ")))

# last_name [1]
personal_data.append(str(input("Ingresa tus apellidos: ")))

# age [2]
personal_data.append(str(input("Ingresa tu edad: ")))

# dpi [3]
personal_data.append(str(input("Ingresa tu No. Dpi o Cui: ")))

#job [4]
personal_data.append(str(input("Ingresa el nombre de la profesión que desempeñas: ")))

# Estado civil [5]
personal_data.append(str(input("Ingrese su Estado Civil (Casad@ o Solter@): ")))

## data handling / Manipulacion de datos por el usuario

# Imprimir los datos actuales
print("Los datos actuales son:\n", personal_data)

# Preguntar al usuario si desea editar un dato
respuesta = input("¿Desea editar un dato? (sí/no): ")

# Unidecode es una libreria que estoy usando en caso
# el usuario inserte un dato con acento
while unidecode(respuesta.lower()) == "si":
    # Si el usuario desea editar un dato, pedirle que ingrese el índice del dato que desea editar
    indice = int(input("Ingrese el numero de la posición del dato que desea editar (1, 2, 3, 4, 5 o 6): "))
    
    # el objetivo de esta variable es hacer accesible el script
    # a las personas que no tengan idea que se parte desde la posicion 0
    indice_traducido = indice - 1

    # Pedirle al usuario que ingrese el nuevo valor para el dato seleccionado
    nuevo_valor = input(f"Ingrese el nuevo valor para {personal_data[indice_traducido]}: ")
    
    # Actualizar el dato en la lista
    personal_data[indice_traducido] = nuevo_valor
    
    # Imprimir los datos actualizados
    print("Los datos actualizados son:\n", personal_data)

    respuesta = input("¿Desea editar un dato? (sí/no): ")

print("No se han realizado cambios en los datos.")
input()