# Iteraciones
# for es una instruccion que permite recorrer un iterable

listasFrutas = ['Pera','Manzana', 'Banano']

for fruta in listasFrutas:
    print(fruta)

    # Utilizar rangos numéricos 

for item in range(0,5):
    print('Elemento{}'.format(item))

matriz = [
    [0,1,0],
    [1,1,1],
    [0,0,2]
]

# Anidados

for fila in matriz:
    for columna in matriz:
        print(columna)

# Anidados basados en indices

for i in range(len(matriz)):
    for j in range(len(matriz[i])):

        #print(type(fila))
        #print(fila)
        print('valor de la posicion i: {} - j: {} es: {}'.format(i,j,matriz[i][j]))

        if matriz[i][j] == 2:
            matriz[i][j] = 10


print(matriz)