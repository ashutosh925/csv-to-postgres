#1
import os
from os import listdir
from os import path

#2
# folder_path = 'filename/'
folder_path = os.curdir # it may have many subfolders and files inside
print(folder_path)
lst = []
from fnmatch import fnmatch
pattern = "*.xlsx"      #I want to get only csv files 

#3
def getModifiedPath(originalPath):
    return ''.join(c for c in originalPath if c.isalpha())

#4
# for filename in listdir(folder_path):
#     src = folder_path + filename
#     dst = folder_path + getModifiedPath(filename[:-5]) + ".xlsx"
#     print(src,dst)
#     #5
#     os.rename(src,dst)
for path, subdirs, files in os.walk(folder_path):
    for name in files:
        if fnmatch(name, pattern):
            src = path
            dst = getModifiedPath(name[:-5])+".xlsx"
            os.rename(src,dst)
            # print(src,dst)  path +"/"+ 
            # read_excel(path,name)
            # print(df)