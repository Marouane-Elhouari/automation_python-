import pandas as pd 
def write_excel(data , path) : 
    df = pd.DataFrame(data)
    df.to_excel(path  , index = False)
    print('excel file created in this path' , path)
    

