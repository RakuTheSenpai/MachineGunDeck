import os
import re

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def sortFilesNumerically(directory_Path, extension):
    i = 1
    for file in sorted(os.listdir(directory_Path), key=numericalSort):
        filename = os.fsdecode(file)
        if filename.endswith(extension):
            if(i>9):
                os.rename(directory_Path + "\\"+filename,directory_Path + "\\"+str(i)+"."+extension)
            else:
                os.rename(directory_Path + "\\"+ filename,directory_Path + "\\0"+str(i)+"."+extension)
            i = i + 1
            continue
