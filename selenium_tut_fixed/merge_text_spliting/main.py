import os 
import shutil
from pathlib import Path

files_folder = 'files'
output_folder = 'output'
merged_folder = os.path.join(output_folder, 'merged.txt')
split_folder = os.path.join(output_folder, 'split.txt')
extract_folder = os.path.join(output_folder, 'extract.txt')

def merge_files() :
    if not os.path.exists(output_folder) : 
        os.makedirs(output_folder)
    with open(merged_folder , 'w' ,encoding = 'utf-8') as file :
        for filename in os.listdir(files_folder) :
            filepath = os.path.join(files_folder , filename)
            if filename.endswith('.txt') :
                with open(filepath , 'r' ,encoding = 'utf-8') as f :
                    file.write(f.read())
                    file.write('\n')
    print(f'MErged files into {merged_folder} successfully')

def split_file():
    if not os.path.exists(split_folder) :
        os.makedirs(split_folder)
        with open(merged_folder , 'r' , encoding = 'utf-8') as file : 
            data = file.read()
        midpoint = len(data) // 2
        port1 = data[:midpoint]
        port2 = data[midpoint:]

        with open(os.path.join(split_folder , 'port1.txt') , 'w' , encoding = 'utf-8') as f1 :
            f1.write(port1)
        with open(os.path.join(split_folder , 'port2.txt') , 'w' , encoding = 'utf-8') as f2 :
            f2.write(port2)
    print(f'Split files into {split_folder} successfully')




def extract_text() :
    if not os.path.exists(extract_folder) :
        os.makedirs(extract_folder)
    with open(merged_folder , 'r' , encoding = 'utf-8') as file :
        data = file.read()
    words = data.split()
    with open(os.path.join(extract_folder , 'extract.txt') , 'w' , encoding = 'utf-8') as f :
        for word in words :
            f.write(word)
if '__name__' == '__main__' :
    merge_files()
    split_file()
    extract_text()