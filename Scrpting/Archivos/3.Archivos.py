# Crear un archivo de texto

with open('Scrpting/Archivos/ejemplo2.txt', mode= 'r+') as miArchivo:
    print(miArchivo.read())
    miArchivo.write('Hola')