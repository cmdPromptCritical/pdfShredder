# Description: Splits a pdf into many files, puts new files in folder named after PDF name in the same dir
# Quick start: use -i (filename) and -dir (file directory) to specify location of file to shred
# Date: 2018-04-30
# Authors: Richard Carlisle, Acamori
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import re
import argparse

## Config
parser = argparse.ArgumentParser(description='Shreds PDF into individual pages.')
parser.add_argument('-dir', nargs=1, default=os.getcwd(),
                   help='select the directory the file is in')
parser.add_argument('-i', nargs=1,
                   help='select the file to be shredded')
args = parser.parse_args()

pdfFile = args.i[0]
pdfDir = args.dir[0]

## functions
def pdf_splitter(index, src_file):
	with open(src_file, 'rb') as act_mls:
		reader = PdfFileReader(act_mls)
		writer = PdfFileWriter()
		writer.addPage(reader.getPage(index))
		outName = pdfFile[:-4] + '_pg' + str(index + 1).zfill(3) + '.pdf'
		try:
			os.makedirs(pdfFile[:-4])
		except:
			pass
		out_file = os.path.join(os.getcwd(), pdfFile[:-4], outName)
		with open(out_file, 'wb') as out_pdf: writer.write(out_pdf)

# gets number of pages
pdf = PdfFileReader(pdfFile)
pages = pdf.getNumPages()

# shreds pdfFile
for x in range(pages): pdf_splitter(x, os.path.join(os.getcwd(), pdfFile))
