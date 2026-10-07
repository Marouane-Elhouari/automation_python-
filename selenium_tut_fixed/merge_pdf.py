from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append('sample.pdf')
merger.append('sample.pdf')
merger.write('merged.pdf')
merger.close()
 