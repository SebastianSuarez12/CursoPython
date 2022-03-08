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