from reportlab.pdfgen import canvas
import PyPDF2

def create_sample_pdf() :
    c = canvas.Canvas('sample.pdf')
    c.drawString(100 , 750 , 'hi im marwan is a chemical engineer and i want to do a fantastic career in this field')
    c.drawString(100 , 700 , 'and im a data scinetist and i want to do a fantastic career in this field')
    c.save()
create_sample_pdf()
with open('sample.pdf' , 'rb') as file :
    reader = PyPDF2.PdfReader(file)
    print(f'the total page is :{  len(reader.pages)}')
    for i , page in enumerate(reader.pages) :
        page = reader.pages[i]
        text = page.extract_text()
        print(f'page {i+1} : {text}')
        

              



