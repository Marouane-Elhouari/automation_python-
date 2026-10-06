import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
#function for aotomate the sorting file
import pathlib as path 
source_folder = path.Path('source_folder') 
source_folder.mkdir(exist_ok=True)
for file in source_folder.iterdir():
    if file.suffix == '.jfif' : 
        folder_images = path.Path('images')
        folder_images.mkdir(exist_ok = True)
        shutil.move(file , folder_images / file.name)


def organize_by_type(folder):
    # Organisation b l-extensions dyal les fichiers
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower() if '.' in filename else 'no_extension'
            ext_folder = os.path.join(folder, ext.upper() + '_files')
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            shutil.move(file_path, os.path.join(ext_folder, filename))

def organize_by_date(folder):
    # Organisation b t-tarikh dyal t-ta3dil
    import time
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            date_str = time.strftime('%Y-%m', time.localtime(mod_time))
            date_folder = os.path.join(folder, 'Date_' + date_str)
            if not os.path.exists(date_folder):
                os.makedirs(date_folder)
            shutil.move(file_path, os.path.join(date_folder, filename))

def start_oarganizing():
    folder = filedialog.askdirectory()
    if not folder:
        return 

    if var.get() == 'type':
        organize_by_type(folder)
        messagebox.showinfo('Success', 'Files organized by type successfully!')
    else:
        organize_by_date(folder)
        messagebox.showinfo('Success', 'Files organized by date successfully!')

root = tk.Tk()
root.title('File Organizer')
root.geometry('350x200')

tk.Label(root, text='Choose how to organize your files', font=('Arial', 12)).pack(pady=20)

var = tk.StringVar(value='type')

radio1 = tk.Radiobutton(root, text='Type', variable=var, value='type', font=('Arial', 12))
radio1.pack()

radio2 = tk.Radiobutton(root, text='Date', variable=var, value='date', font=('Arial', 12))
radio2.pack()

button = tk.Button(root, text='Organize', command=start_oarganizing, bg='#4CAF50', fg='white', font=('Arial', 12))
button.pack(pady=20)

root.mainloop()