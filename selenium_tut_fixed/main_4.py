from excel.read_excel import read_excel
from excel.write_excel import write_excel
from pdf.read_pdf import read_pdf
from pdf.create_pdf import create_pdf

data = read_excel(r'C:\Users\pc\Downloads\selenium_tut_fixed\selenium_tut_fixed\excel_demo.xlsx')

write_excel([{'Name' : 'John' , 'Age' : 30 , 'City' : 'New York'}] , r'C:\Users\pc\Downloads\selenium_tut_fixed\selenium_tut_fixed')

create_pdf('hada marwan inchallah he will do a fantastic career in engineering' , r'C:\Users\pc\Downloads\selenium_tut_fixed\selenium_tut_fixed\pmarwan.pdf')

read_pdf(r'C:\Users\pc\Downloads\selenium_tut_fixed\hello.pdf')
