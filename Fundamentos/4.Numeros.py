# Enteros  -> int
# Conversiones de datos

# Importaciones 
import math as math

num1 = input('Ingresa un numero: ') # num es tipo str
print(type(num1))

num1 = int(num1) # Conversion a entero
print(type(num1))
print(num1)

# En una sola linea de codigo, tomo la entrada de input y la convierto a entero

num2 = int(input('Ingrese otro numero: '))
print(num2 + 2)

#
num3 = int(True)
#True -> 1
#False -> 0
print(num3)

# Operadores numéricos
a, b = 2, 3
# Suma 
print('\t Operaciones con numeros')
print('Suma: ', a + b)
# Resta
print('Resta', a - b)
# Multiplicacion
print('Multiplicacion', a * b)
#División
print('Division', a / b)
#Division de dos numeros siempre será un numero flotante

# Potencia
print('Potencia', 2**3)

# Módulo
print('Modulo', a%b)

# Division entera
print('Division entera', 10//3)

# Raiz 
print('Raiz', 64 ** (1/2))
print('Raiz', math.sqrt(64))

#-----------------------------------------------
# Floats - > float, consideraciones separación con el punto .
#-----------------------------------------------

numeroFlotante = float(input('Ingresa un numero decimal: '))
print(numeroFlotante)
# Operadores son los mismos que los enteros