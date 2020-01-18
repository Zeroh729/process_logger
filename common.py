import os

def findLastIndex(s, ch):
    indices = [i for i, ltr in enumerate(s) if ltr == ch]
    if indices != []:
        return indices[-1]
    return -1

def createDir(path):
    directory = getDirectory(path)
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def listFilePaths(directory=os.getcwd(), **kwargs):
    filepaths = []
    for root, directories, files in os.walk(directory):
        for f in files:
            filepath = os.path.join(root, f)
            if("filterName" in kwargs.keys()):
                if(kwargs['filterName'] in filepath):
                    filepaths.append(filepath)
            else:
                filepaths.append(filepath)
    return filepaths

def getDirectory(path):
    directory = ""
    if "/" in path:
        directory = path
        if('.' in path):
            directory = path[:findLastIndex(path, "/")]
    return directory