from __future__ import print_function
import logging
from common import createDir

class ProcessLogger:
    def __init__(self, filename, isMainProcess=False):
        self.log = ""
        self.isMainProcess = isMainProcess
        if(self.isMainProcess):
            createDir(filename)
            self.__configLogging("main", filename, printToConsole=True)
        else:
            self.__configLogging("process", filename)

    def print(self, *args, **kwargs):
        newlog = ' '.join(str(a) for a in args)
        self.log += newlog +"\n"
        if(self.isMainProcess):
            logging.getLogger("main").info(newlog)
        else:
            logging.getLogger("process").info(newlog)

    def printToMain(self):
        logging.getLogger("main").info(self.log)

    def getLog(self):
        return self.log

    def __configLogging(self, loggername, logfilename, printToConsole = False):
        logging.basicConfig(filename=logfilename,
                            level=logging.INFO,
                            format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
        if printToConsole:
            import sys
            log = logging.getLogger(loggername)
            log.addHandler(logging.StreamHandler(sys.stdout))