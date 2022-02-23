# Diccionarios -> dict()
# Hash maps 

# Tiene dos partes: clave(llave) y el valor
# Tras la inicialización la clave es inmutable
# Clave puede ser de cualquier tipo de dato
# No soporta la indexación
# CRUD 

diccionario1 = {
    'i1' : 1,
    'i2' : 5
}

print(type(diccionario1))
print(diccionario1)

# print(diccionario1[0]) # error
print(diccionario1['i2'])

edad = 19

persona = {
    'nombre' : 'Andres',
    'apellido' : 'Suarez',
    'edad' : edad,
    21 : 12,
    'casado' : False,
    'llevaVariable' : '1004567879'
}

print(persona['nombre'])

materias = {
    'auditoriaInformatica' : 8,
    'webAvanzado2' : 7
}



# Agregar un elemento al diccionario
print('Metodos')
# obtener un valor
print(persona.get('edad'))
# actualizar un dato
print(persona.update({'edad':23}))
print(persona)
# Agregar un valor a un diccionario ya creado
persona['universidad'] = 'EPN'
print(persona)
# eliminar valores de un diccionario
persona.pop(21)
print(persona)
# pop eliminacion del valor 

# 1. Saber cuales son los valores del diccioanrio
print(persona.values())
# 2. Saber cuales son solo las llaves del diccionario
print(persona.keys())
# 3. Diccionario mapeado 
print(persona.items())

def obtenerLlave(valorBuscar):
    for llave, valor in persona.items():
        if valorBuscar == valor:
            return llave
print('Llave encontrada: ', obtenerLlave('1004567879'))

persona.pop(obtenerLlave('1004567879'))
print(persona)

# pop item -> eliminar el ultimo valor insertado en el diccionario (3.7)
# pop item -> removia un valor randómico
# pop item -> randomico con numeros
persona.popitem()
print(persona)

# Que pasaria si pido obtener un valor 
print(persona.get('mascota', 'No existe ese valor'))

copiaPersona = persona.copy()
print(copiaPersona)

# Numerable 
print(len(copiaPersona))

# eliminar todo
copiaPersona.clear()
print(copiaPersona)
# conversion entre lista y diccioanrio

# 1

listaPrueba = [0,1,2,3,4]
diccionarioPrueba = {}

for i in listaPrueba:
    diccionarioPrueba[i] = i

print(diccionarioPrueba)

# 2
diccionarioPrueba2 = {}
listaLlave = ['n0', 'n1', 'n2', 'n3', 'n4']
listaPrueba2 = [0,1,2,3,4]

for i in range(len(listaLlave)):
    diccionarioPrueba2[listaLlave[i]] = listaPrueba2[i]
print(diccionarioPrueba2)

# 3
diccionarioPrueba3 = dict(zip(listaLlave, listaPrueba2))
print(diccionarioPrueba3)

