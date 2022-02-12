# Si, sino, entonces
# If, else y elif

from fcntl import F_SEAL_SEAL


variable1 = True
variable2 = False

# Operador
# 1

print(1 == 1)
print('Hola' == 'Hola')
print('Hola' == 'hola')

if variable1 and variable2 == True:
    # False == True
    print('La expresion es verdadera')
else:
    print('La expresion es falsa')

# Comprobaciones

texto = 'Andrés'

# Python se puede omititr la comparacion a verdader
# if texto.startswith('A') == True:
# es igual a escribir
if texto.startswith('A'):
    print('Tu nombre empieza con A')

elif texto.startswth('B'):
    print('Tu nombre empieza con la B')

else:
    print('Tu nombre no empieza con la letra A')


# Otro tipo de comparaciones
print(10 > 20)
print(500 != 200)
print('Andres' != 'Sebastian')    

x = 10
print(0 < x < 12)  #Intervalos
print(4 < 5 < 8 < 200)

print('A' > 'B')  # Toma en cuenta el alfabeto
print( 'oso' < 'osa')  # revisa todos los caracteres

