# Conjuntos -> set
# sets

conjunto1 = {1,2,3,4}
print(conjunto1)
print(type(conjunto1))

conjunto2 = {1,2,3,4,4}
print(conjunto2)

# Crear una lista con elementos unicos
listaEjemplo = [14,15,16,63,63,63,89,75,14,15]
conjunto3 = set(listaEjemplo)
print(conjunto3)
listaElementosUnicos = list(conjunto3)
print(listaElementosUnicos)

conjunto3 = list(set(listaEjemplo))   # Esto es lo mismo que arriba
print(conjunto3)

# ¿Es posible crar conjuntos no numéricos?

conjunto4 = {'Andres', 'Bryan', 'Cristo', 'Andres'}
print(conjunto4)

# ¿Es posible crear conjuntos de diferentes tipos de datos?
conjunto5 = {78,59235.2, True, False, 'Anderson'}
print(conjunto5)

# Métodos de los conjuntos
cA = {1,2,3,4,5,6,7}
cB = {3,4,5}

# Agregar un elemento al conjunto
cA.add(8)
print(cA)

# Averiguar el tamaño de un conjunto (cardinalidad)
print(len(cA))

# Eliminar un elemento del conjunto
cA.discard(8)
print(cA)

# Update conjunto
cA.update({6,7,8,9})
print(cA)

# Copiar un conjunto
cD = cA.copy()
print(cD)

# pop , elimina el primer elemento
cD.pop()
cD.pop()
print(cD)

# Limpiar
cD.clear()
print(cD)

# Método entre dos conjuntos
print('Conjunto A: ', cA)
print('Conjunto B: ', cB)

print(' Diferencia: ',cA.difference(cB))

# G = {1,2,3,4,5}
# H = {1,2,3}
# diferencia entre G y H seria G-H

# Unión
cC = {10}
print('Union: ',cA.union(cC))

# Intersección
print('Interseccion: ',cA.intersection(cB))

# Simetria
print('Diferencia simetrica: ',cA.symmetric_difference(cB))

# Si dos conjuntos son disjuntos
print(cA.isdisjoint(cB))
cE = {100, 20, 23}
print(cA.isdisjoint(cE))

# Averiguar si es subconjunto
print(cB.issubset(cA))

# Averiguar si es superconjunto
print(cA.issuperset(cB))