import PyPDF2

archivoPdf = PyPDF2.PdfFileReader((open('Scrpting/PDF/unionEjemplo.pdf', 'rb')))
marcaAgua = PyPDF2.PdfFileReader((open('Scrpting/PDF/marcaAgua.pdf', 'rb')))
paginaMarcaAgua = marcaAgua.getPage(0)
salida = PyPDF2.PdfFileWriter()


for numeroPaginas in range(int(archivoPdf.getNumPages())):
    page = archivoPdf.getPage(numeroPaginas)
    page.mergePage(marcaAgua.getPage(paginaMarcaAgua))
    salida.addPage(page)

with open('Scrpting/PDF/resultadoFinal.pdf','wb') as archivoFinal:
    salida.write(archivoFinal)

