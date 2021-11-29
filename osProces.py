import sys,os
try:
    import pandas as pd
    from openpyxl import load_workbook
    import zipfile
    import io
except:
    os.system("pip3 install openpyxl pandas")

    
root = os.curdir # it may have many subfolders and files inside
lst = []
from fnmatch import fnmatch
pattern = "*.xlsx"      #I want to get only csv files 
# pattern = "*.*"        # Note: Use this pattern to get all types of files and folders 

def getModifiedPath(originalPath):
    return ''.join(c for c in originalPath if c.isalpha())

def read_excel(path,name):
    try:
        # wb = load_workbook(path+"/"+name,read_only=True)
        return pd.read_excel(path+"/"+name,engine='openpyxl',encoding='utf-8')
    except Exception as error:
        print(error)
        # file =zipfile.ZipFile(path+"/"+name)
        # file_name = file.namelist()[0]
        # df = pd.read_excel(file.open(file_name).read())
        # print(df.head(1))
        # src = path + name
        # path + 
        # dst = getModifiedPath(name[:-5]) + ".xlsx"
        # print(dst)
        # os.rename(src,dst)
        # read_excel(path,getModifiedPath(name[:-5]) + ".xlsx") 

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            read_excel(path,name)
            # print(df)
            

            
        
# print((os.path.join(path, name)))
# lst.append((os.path.join(path, name)))
# df = pd.DataFrame({"filePaths":lst})
# print(df.head(1))


