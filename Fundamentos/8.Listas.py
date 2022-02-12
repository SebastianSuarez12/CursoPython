# Listas list()
# Inicializacion []
# Listas no tiene un espacio definido

lista1 = [1,2,3,4,5,6,7,8,9,10]
print(type(lista1))

# Listas combinadas 
lista2 = ['a','b','c',85,54, True, 35.78]
print(lista2)

# Métodos y las operaciones de las listas

# Indexación
# averiguar largo o número de elementos que tiene una lista
print(len(lista2))
print(lista2[0])
print(lista2[6])

# Cambiar los valores de la lista

lista2[5] = False
print(lista2)

# Indexacion entre intervalos
print(lista2[1:3])
print(lista2[::-1])

# Lista de alumnos

listaAlumnos = ['Anderson','Andres','Cristo','Janeth','Mario']

# Obtener una nueva lista con las dos ultimas personas

listaAlumnos2 = listaAlumnos[1:]
print(listaAlumnos2)
print(type(listaAlumnos2))

# Agregar datos al final de una lista
listaAlumnos2.append('Fernanda')
print(listaAlumnos2)

# agrega datos en una posicion en especifico
listaAlumnos2.insert(3,'Bryan')
print(listaAlumnos2)

# Como agregar al final otra lista

listaAlumnos2.extend(['Pablo','Jose'])
print(listaAlumnos2)

# Retirar elementos
# pop recibe el indice que quiero retirar
# pero si no le paso el índice retira el último elemento
listaAlumnos2.pop()
print(listaAlumnos2)

# remover con un índice en específico
listaAlumnos2.pop(1)
print(listaAlumnos2)

# retiramos un valor en especifico de la lista
listaAlumnos2.remove('Pablo')
print(listaAlumnos2)

# ¿Qué pasa si hay dos elementos con el mismo nombre?
listaAlumnos2.extend(['Alejandro','Alejandro'])
print(listaAlumnos2)
listaAlumnos2.remove('Alejandro')
print(listaAlumnos2)

# OPerador 
print('Andres' in listaAlumnos2)

# Hacer una copia
copiaListaAlumnos = listaAlumnos2[::]
print(copiaListaAlumnos)
copiaListaAlumnos2 = listaAlumnos2.copy()
print(copiaListaAlumnos2)

# Invertir la copia 
print(copiaListaAlumnos[::-1])
copiaListaAlumnos2.reverse()
print(copiaListaAlumnos2)

# Encontre indice de un elemento
print(copiaListaAlumnos.index('Janeth'))

# ¿Qué pasaria si solicito un índice de un elemento que no se encuentra en la lista?
# print(copiaListaAlumnos.index(58))
# producira un error si el lelemnto no se encuentra enlistado

# Ordenar
copiaListaAlumnos.sort()
print(copiaListaAlumnos)

lista4 = [85,47,68,25]
lista4.sort(reverse = True)
print(lista4)

# Ordenar una lista con diferentes tipos de datos no es posible 
# lista5 = ['A', 58,68]
# lista5.sort()
# print(lista4)

# Pueden convertir un string a lista
cadenaTexto = 'Las universidades piensas en retornar a la presencialidad'
listaTexto = list(cadenaTexto)
# print(listaTexto)

# Separador en palabras
listaPalabras = cadenaTexto.split(' ')
print(listaPalabras)

# contar el numero de veces que una palabra esta en la lista

print(listaPalabras.count('universidades'))

# join 
saludo = 'Saludo: '
oracion = saludo.join([' buenos dias', ' buenas tardes'])
print(oracion)

lista5 = ['Hola']
lista6 = ['cómo estas?']
temp = lista5.extend(lista6)
temp = str(temp)
print(temp)

# Declarar una lista vacia
lista7 = []

# eliminar todos los elementos de una lista 
# temp.clear()
print(temp)

# Unpacking, desempaqeutado de una lista
print(listaAlumnos)
nombre1, nombre2, = listaAlumnos[0:2]
print(nombre1)
print(nombre2)

nombre1, nombre2, *nombres = listaAlumnos

print(nombre1)
print(nombre2)
print(nombres)

# Lista de listas

matriz = [
    [0,1,1],
    [1,1,1],
    [0,0,2]
]

print(matriz)
print(matriz[2][2])