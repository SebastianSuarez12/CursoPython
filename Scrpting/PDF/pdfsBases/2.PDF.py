# Unir pdfs

import PyPDF2

def unir_pdfs(listaPdfs: list, nombrePdf: str):
    merger = PyPDF2.PdfFileMerger()

    for pdf in listaPdfs:
        merger.append(pdf)

    merger.write('Scrpting/PDF/' + nombrePdf+'.pdf')


lista = ['Scrpting/PDF/pdfsBases/pdfUnido.pdf','Scrpting/PDF/pdfsBases/pdfBlanco.pdf']
unir_pdfs(lista, 'unionEjemplo')