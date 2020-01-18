from __future__ import print_function
import logging
import os
from common import createDir, listFilePaths

logfilename = None

def init(filename):
    global logfilename
    logfilename = filename
    createDir(logfilename + ".log")

    logging.basicConfig(filename=logfilename + ".log",
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')

def log(*args):
    if(logfilename != None):
        logging.info(getMsg(args))

def writeOutput(*args):
    if(logfilename != None):
        outputFilename = logfilename + "_pid" +  str(os.getpid()) + ".log"
        with open(outputFilename, "a+") as f:
            f.write(getMsg(args) + "\r\n")

def mergeOutputs():
    global logfilename
    filepaths = listFilePaths(filterName=logfilename)
    mainOut = next((x for x in filepaths if str(os.getpid()) in x), None)
    
    with open(logfilename + "_output.txt", "w+") as outF:
        for filepath in filepaths:
            with open(filepath) as f:
                outF.write(f.read() + "\r\n")

def getMsg(args):
    return ' '.join(str(a) for a in args)