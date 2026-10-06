import PyPDF2

def read_pdf(file_path): 
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i , page in enumerate(reader.pages) : 
            print(f'page {i} : {page.extractText()}')