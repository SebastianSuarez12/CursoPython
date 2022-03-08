# 1. Crear un script que genere un archivo con elementos repetidos

import random

deportes = ['Futbol','Tenis','Basket','BalonMano','Karate','Atletismo']

for i in range(100):
    print(random.choice(deportes))

# Creacion de archivo desde python
archivo = open('Scrpting/Archivos/ejercicio.txt','w')
archivo.close()

# Escribir su contenido

with open('Scrpting/Archivos/ejercicio.txt', mode= 'r+') as miArchivo:

    for i in range(500):
        miArchivo.write(random.choice(deportes) + '\n')

#-----------------------------------------------------------------------------------------

# Crear un nuevo archivo llamado resumen.txt

# Cabecera

# Elemento ocurrencias
# Futbol  25
# Baket   30
futbol = 0
basket = 0
tenis = 0
balonMano = 0
karate = 0
atletismo = 0

resumen = open('Scrpting/Archivos/resumen.txt','w')

with open('Scrpting/Archivos/resumen.txt', mode= 'r+') as resumen:

    for i in range(500):
        resumen.write(random.choice(deportes) + '\n')

    resumen.seek(0)
    aux = resumen.readlines()

    for i in range(len(aux)):
        
        if aux[i] == 'Futbol\n':
            futbol = futbol + 1
        if aux[i] == 'Basket\n':
            basket = basket + 1
        if aux[i] == 'Tenis\n':
            tenis = tenis + 1
        if aux[i] == 'BalonMano\n':
            balonMano = balonMano + 1
        if aux[i] == 'Karate\n':
            karate = karate + 1
        if aux[i] == 'Atletismo\n':
            atletismo = atletismo + 1

    resumen.write('\n\n --Elementos ocurrencias-- \n')
    resumen.write('\nFutbol: ' + str(futbol))
    resumen.write('\nBasket: ' + str(basket))
    resumen.write('\nTenis: ' + str(tenis))
    resumen.write('\nBalonMano: ' + str(balonMano))
    resumen.write('\nKarate: ' + str(karate))
    resumen.write('\nAtletismo: ' + str(atletismo))