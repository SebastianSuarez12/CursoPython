# Programa que permita resolver una ecuacion de segundo grado
# ax2 + bx + c = 0 // a, b y c son numeros enteros
#Pedir al usuario que ingrese los valores de a, b y c
#Imprime en consola la ecuacion de segundo grado
#Mostrar las 2 soluciones x1, x2
import math

print('La ecuacion tiene la forma de ax^2 + bx + c  = 0')
a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

print('La ecuacion resultante es: ', a,'x^2+',b,'x+',c,'= 0')

x1 = (-b +math.sqrt((b**2) - (4*a*c))) / (2*a)
x2 = (-b -math.sqrt((b**2) - (4*a*c))) / (2*a)

print('El valor de x1 es: ', x1)
print('El valor de x2 es: ', x2)



