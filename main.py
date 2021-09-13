from copy import deepcopy
from PyPDF2 import *
from pathlib import Path
from os import listdir

from PyPDF2.pdf import PdfFileReader, PdfFileWriter


def main():
    for file in listdir():
        if file[-4:] == ".pdf" and file[-9:] != "_wide.pdf":
            widenPDF(file)


def widenPDF(fileName):
    pdf = PdfFileReader(fileName)
    
    N = pdf.getNumPages()
    
    pdfWriter = PdfFileWriter()
    for i in range(N):
        page = pdf.getPage(i)
        width = page.mediaBox.lowerRight[0] - page.mediaBox.lowerLeft[0]
        
        page.mediaBox.lowerRight = (page.mediaBox.lowerLeft[0] + 2*width, page.mediaBox.lowerRight[1])
        page.cropBox.lowerRight = (page.cropBox.lowerLeft[0] + 2*width, page.cropBox.lowerRight[1])
        page.artBox.lowerRight = (page.artBox.lowerLeft[0] + 2*width, page.artBox.lowerRight[1])
        page.bleedBox.lowerRight = (page.bleedBox.lowerLeft[0] + 2*width, page.bleedBox.lowerRight[1])
        pdfWriter.addPage(page)
    
    with Path(fileName[:-4] + "_wide.pdf").open(mode="wb") as outputFile:
        pdfWriter.write(outputFile)
    

if __name__ == "__main__":
    main()