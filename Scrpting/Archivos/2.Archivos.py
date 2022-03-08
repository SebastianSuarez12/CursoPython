# Manejar archivos con with

with open('Scrpting/Archivos/ejemplo.txt', 'r+') as miArchivo:
    # Todas las acciones
    print(miArchivo.read())
    # Escribir un archivo
    # Write reemplaza el contenido y lo escribe en el archivo
    miArchivo.write('\nTexto escrito desde mi script 2')
    miArchivo.seek(0)
    print(miArchivo.read())


