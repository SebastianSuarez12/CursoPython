import PyPDF2 as pdf
from nbformat import write
# forma de abrir archivos
# textual
# binario
archivo = 'Scrpting/PDF/pdfsBases/pdfUnido.pdf'

with open(archivo, 'rb') as miArchivo:
    print(miArchivo)
    print(type(miArchivo))

    # pasar esta inforamción binario 
    # a un formato operable para pdf

    archivoPDF = pdf.PdfFileReader(miArchivo)
    print(archivoPDF)
    print(type(archivoPDF))

    # Informacion archivo pdf
    print(f'Info del archivo {archivo} es: {archivoPDF.getDocumentInfo()}')

    # Número de páginas
    print(f'Número de páginas del archivo {archivo} es: {archivoPDF.getNumPages()} ' )

    # Obtener una página en específico

    pagina = archivoPDF.getPage(0)
    print(pagina)
    print(type(pagina))

    # Rotar una página
    pagina.rotateCounterClockwise(180)

    # Escribir pdf

    writerPdf = pdf.PdfFileWriter()
    writerPdf.addPage(pagina)
    #writerPdf.addBlankPage()

    with open('Scrpting/PDF//pdfBlanco.pdf', 'wb') as pdfSalida:
        writerPdf.write(pdfSalida)