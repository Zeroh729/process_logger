from __future__ import print_function
import logging
import os
from common import createDir, listFilePaths

logfilename = None
process_ids = []

_FORMAT = '%(asctime)s - %(message)s'
_DATEFMT = '%m/%d/%Y %I:%M:%S%p'
def init(filename):
    global logfilename
    logfilename = filename
    createDir(logfilename + ".log")

    logging.basicConfig(filename=logfilename + "_log_all.log",
                        level=logging.INFO,
                        format=_FORMAT, datefmt=_DATEFMT)

def initProcess():
    if(os.getpid() not in process_ids):
        process_ids.append(os.getpid())
        filename = "{}_log_{}.log".format(logfilename, os.getpid())
        createDir(filename)
        formatter = logging.Formatter(fmt=_FORMAT, datefmt=_DATEFMT)
        filehandler = logging.FileHandler(filename)
        filehandler.setFormatter(formatter)
        logger = logging.getLogger("subprocess_{}".format(os.getpid()))
        logger.addHandler(filehandler)

def __logging():
    return logging.getLogger("subprocess_{}".format(os.getpid()))

def log(*args):
    if(logfilename != None):
        __logging().info(getMsg(args))

def writeOutput(*args):
    if(logfilename != None):
        outputFilename = logfilename + "_out_" +  str(os.getpid()) + ".txt"
        with open(outputFilename, "a+") as f:
            f.write(getMsg(args) + "\r\n")

def mergeOutputs():
    global logfilename
    filepaths = listFilePaths(filterName=logfilename + "_pid")
    mainIndex = next((i for i,x in enumerate(filepaths) if str(os.getpid()) in x), None)
    if(mainIndex != None):
        filepaths.insert(0, filepaths.pop(mainIndex))

    with open(logfilename + "_out_merged.txt", "w+") as outF:
        for filepath in filepaths:
            with open(filepath) as f:
                outF.write(f.read() + "\r\n")

def getMsg(args):
    return ' '.join(str(a) for a in args)