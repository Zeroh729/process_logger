from __future__ import print_function

def findLastIndex(s, ch):
    indices = [i for i, ltr in enumerate(s) if ltr == ch]
    if indices != []:
        return indices[-1]
    return -1

def createDir(path):
    if "/" in path:
        directory = path
        if('.' in path):
            directory = path[:findLastIndex(path, "/")]
        import os
        if not os.path.exists(directory):
            os.makedirs(directory)