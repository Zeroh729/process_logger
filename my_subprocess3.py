import os
import time

import process_logger as pl

def initLogging(logfilename):
    pl.init(logfilename)

def run_worker():
    pl.log("my_subprocess3 started by", os.getpid())
    print(os.getpid(), " - Beep boob.")
    subfunc()

def subfunc():
    print(os.getpid(), " - I was called by another module!")

if __name__ == "__main__":
    run_worker()