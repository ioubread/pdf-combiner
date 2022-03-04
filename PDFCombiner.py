import sys
from PyPDF2 import PdfFileMerger
import os

targetFilesToCombine = sys.argv[1:]

targetFilesToCombine.sort()

commonName = os.path.commonprefix(targetFilesToCombine)
finalName = commonName + ".pdf"

merger = PdfFileMerger()


for pdf in targetFilesToCombine:
    merger.append(pdf)



merger.write(finalName)
merger.close()