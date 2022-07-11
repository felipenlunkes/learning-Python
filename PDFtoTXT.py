#!/usr/bin/python3
#
# Created by Felipe Miguel Nery Lunkes (10/07/2022)
#
# pip install PyPDF2

import PyPDF2

PDFname=input('PDF name: ')
PDFFile=open(PDFname, "rb")
print('Converting PDF', PDFname, 'into TXT...')
PDFContent=PyPDF2.PdfFileReader(PDFFile)
PDFPages=len(PDFContent.pages)
TXTFile=open('PDFToTXT.txt', "w")

# Loop to read all the pages

for x in range(0, PDFPages-2):
    PDFPage=PDFContent.getPage(x)
    TXTContent=PDFPage.extractText()
    TXTFile.write(TXTContent)

exit()

