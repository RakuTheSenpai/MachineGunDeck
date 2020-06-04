import os 
def getUsers(anki_Roaming_Path):
    return [dirname for dirname in os.listdir(anki_Roaming_Path) if 'addon' not in dirname and os.path.isdir(anki_Roaming_Path + "\\" + dirname)]
def getDictionaries(anki_dictionaries_Path):
    dictionaries = [dictionary for dictionary in os.listdir(anki_dictionaries_Path)]
    return [ os.listdir(anki_dictionaries_Path + "\\"+dictionary)[0] for dictionary in dictionaries]
