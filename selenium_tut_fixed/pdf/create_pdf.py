from fpdf import FPDF
def create_pdf(txet , outpur_file )  :
    pdf =FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size =13)
    pdf.multi_cell(190 , 12 ,txt = txet )
    pdf.output(outpur_file)
    print('pdf file created in this path' , outpur_file)