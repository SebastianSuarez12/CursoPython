# Booleanos
# Dos tipos
# False y True

# True -> 1
# False -> 0
from enum import Flag


variable1 = True
variable2 = False

print(type(variable1))
print(variable1.bit_length())

# Operadores
# Asignacion =
# Aritmeticos
# String + -> concatenación

# Asignacion complementaria
x = 4
x += 5 # le sumo 5 -> x = x + 5
print(x)
x**=2
print(x)

# Operadores lógicos

# Conjunción -> y
print(variable1 and variable2) 
print(True and True)
print(False and False)

# Disyuncion -> or
print('OR')
print(variable1 or variable2)
print(False or False)

# Negacion -> not
print(not variable1)
print(not variable2)

# Ejemplo
print(4 ^ 5)  # Convertir a bianrio y de ahi hacer la operacion
print('1: ', True ^ True)  # -> False
print('2: ', True and True)  # -> True  # Operacion logica de toda la expresion
# Operaciones bit a bit
# AND
print(True & True) # 3. Tomar el truly or falsy y hacer la operacion and

# OR
print(4 | False)

# Operador xor
print(4 ^ 5) #  1 ^ 1 1. convertir a binario y de ahi hacer la operacion

# Not 
print(~False)

# Desplazamineto de bit a bit hacia la derecha
print(True >> False)

# Desplazamiento bit a bit hacia la izquierda
print(True << False)


# Operadores bit a bit
# Base 10 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Binario -> 0, 1
# Hexadecimal, octal
# 1 Byte -> 8 bits

# 10101010 -> 1 byte

#   101
# & 000
#   ---
#   000

#   1101
# & 1001
#   ----
#   1001

# Ejemplo de los operadores bit a bit

var1 = 2 # 10
var2 = 3 # 011
var3 = 5 # 101

print('Probando los binarios')
print( var1 & var2)

# var1 ->  10
# var2 -> &11
#         ---
#          10   -> 2
# base 10

print(var1 | var2)
# var1 ->  10
# var2 -> |11
#         ---
#          11  -> 3(base 10)

print(var1 ^ var2)
# var1 ->  10
# var2 -> ^11
#         ---
#          01  -> 1(base 10)

print( ~var1)
# var1 -> 00000010
#        ~11111101

print( var1 >> var2)
#   10
#   11
#    0


# Operadores de Pertenencia
# Identidad