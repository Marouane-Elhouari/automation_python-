import os 
from pathlib import Path
from datetime import datetime

folder_path = 'sample_files'
if not os.path.exists('sample_files'):
    os.makedirs('sample_files')
else : 
    print('folder already exists')

file_path = os.path.join(r"C:\Users\pc\Desktop\project\sending_msg", "sample_files")

today = datetime.today().strftime('%d-%m-%Y')

for index , filename in enumerate(os.listdir(file_path)):
    old_path = os.path.join(file_path  , filename)
    if os.path.isfile(old_path) :
        _ , ext = os.path.splitext(filename)
        new_name = f'{today}_{index}{ext}'
        new_path = os.path.join(file_path , new_name)
        os.rename(old_path , new_path)
        print(f'file {filename} renamed to {new_name}')
print('files renamed')

    
