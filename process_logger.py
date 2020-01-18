from __future__ import print_function
import logging
from common import createDir
import __builtin__
import os

__logfilename = None
TEMP_DIR = "__temp__/"

def init(logfilename):
    global __logfilename
    __logfilename = logfilename
    createDir(__logfilename)
    createDir(__getSubprocessLogFilename())
    __configLogging("logonly", __logfilename + ".log")

def initSubprocess(logfilename):
    global __logfilename
    __logfilename = logfilename
    createDir(__getStdoutLogFilename())
    __configLogging(__getSubLoggername(), __getSubprocessLogFilename(), noFormat = True)
    __configLogging("stdout", __getStdoutLogFilename(), printToConsole=True)

def print(*args, **kwargs):   
    try:
        logging.getLogger("stdout").info(' '.join(str(a) for a in args))
    except TypeError:
        __builtin__.print("Error - have you initialized process_logger.py?")

def __print(*args, **kwargs):
    logging.getLogger(__getSubLoggername()).info(' '.join(str(a) for a in args))

def log(*args):
    if(__logfilename != None):
        logging.getLogger("logonly").info(' '.join(str(a) for a in args))

def __getSubLoggername():
    return "subprocess_" + str(os.getpid())

def __getSubprocessLogFilename():
    return TEMP_DIR+__logfilename+"_temp_" + str(os.getpid()) + '.log'
    
def __getStdoutLogFilename():
    return TEMP_DIR+__logfilename+"_stdout.log"

def __configLogging(loggername, logfilename, **kwargs):
    if os.path.isfile(logfilename):
        return
    format = '%(asctime)s - %(message)s'

    if 'noFormat' in kwargs.keys():
        if kwargs['noFormat']:
            format = '%(message)s'
            
    handler = logging.FileHandler(logfilename)        
    handler.setFormatter(logging.Formatter(format, datefmt='%m/%d/%Y %I:%M:%S%p'))

    logger = logging.getLogger(loggername)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    if 'printToConsole' in kwargs.keys():
        if kwargs['printToConsole']:
            import sys
            logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.info("")
        
def releasePrints():
    filename = __getSubprocessLogFilename()
    with open(filename, 'r') as f:
        logging.getLogger("stdout").info(f.read())
    with open(filename, 'w') as f:
        f.write("")
    
def cleanup():
    for r, d, f in os.walk(TEMP_DIR):
        for file in f:
            filepath = os.path.join(r, file)
            if __logfilename in filepath:
                os.remove(filepath)