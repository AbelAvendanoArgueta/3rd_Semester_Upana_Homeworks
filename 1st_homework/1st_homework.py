# var  type int
"""
Variables en Python
Due March 3, 2023 11:59 PM
Closes March 3, 2023 11:59 PM

Instructions: 
Crear un script que contenga los siguientes tipos de variables: 

    - Entero (int)
    - Coma flotante (float)
    - Complejo (complex)
    - Booleano (bool)
    - Texto (String) 
    - Texto (String) utilizando salto de linea con diagonal
"""

var_int = 255
print(type(var_int)) # --- python will transform this var to string in order to print

# var type float

var_float = 255.00
print(type(var_float))

# variable complex

var_complex = 5 + 5j
print(type(var_complex))

# variable bool

var_bool = True
print(type(var_bool))

# var type string

var_string = "Hola"
print(type(var_string))

# var type strin using \

var_string_extra = ("Hola \nComo estas?")
print(var_string_extra)
# variable int to hex

var_intTo_hex = 255
print("Valor en hexadecimal:", hex(var_intTo_hex))

# variable hex to int

var_hexTo_int = "FF"
var_traducida = int(var_hexTo_int, 16)
print("Valor numerico traducido desde hexadecimal:", var_traducida)