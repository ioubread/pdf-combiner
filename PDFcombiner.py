# from pathlib import Path
from PyPDF2 import PdfFileMerger
import os
# import sys


pdfs = os.listdir(".")

pdfs.sort()

# selfname = os.path.basename(__file__)

selfname = "PDFcombiner.exe"

try:
    
    pdfs.remove(selfname)
except:
    pass

merger = PdfFileMerger()


for pdf in pdfs:
    merger.append(pdf)


merger.write("rename.pdf")
merger.close()
