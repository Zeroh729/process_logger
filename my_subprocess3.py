from __future__ import print_function
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__
import os
import time
import process_logger

def initLogging(logfilename):
    global print
    process_logger.initSubprocess(logfilename)
    print = process_logger.__print

def run_worker():
    print(os.getpid(), " - Beep boob.")
    subfunc()

def subfunc():
    print(os.getpid(), " - I was called by another module!")

if __name__ == "__main__":
    run_worker()