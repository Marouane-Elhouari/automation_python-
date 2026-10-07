import os 
import shutil

folder_path = r'C:\Users\pc\Desktop\project\sending_msg\files'

files_types = {
        'Images' : ['.jpg' , '.png' , '.jpeg'  , '.gif'] , 
        'Documents' : ['/pdf' , '.doc' , '.docx' , '.txt']  ,
        'Videos' : ['.mp4' , '.mkv' , '.flv'] , 
        'Audios' : ['.mp3' , '.wav' , '.ogg'] , 
        'Archives' : ['.rar' , '.zip']


}

for folder in files_types.keys():
    os.makedirs(os.path.join(folder_path , folder) , exist_ok  = True )

for filename in os.listdir(folder_path) : 
    file_path = os.path.join(folder_path , filename)
    if os.path.isfile(file_path) : 
        for ext in files_types.values():
            for _ext in ext:
                if filename.endswith(_ext):
                    shutil.move(file_path , os.path.join(folder_path , folder))
                    break


