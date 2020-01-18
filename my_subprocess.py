from __future__ import print_function
try:
    import __builtin__
except (ImportError, ModuleNotFoundError):
    import builtins as __builtin__
import os
import time
import my_subprocess3
import process_logger

def initLogging(logfilename):
    global print
    process_logger.initSubprocess(logfilename)
    print = process_logger.__print

def run_worker(delay):
    print("--------------------------------------------------------")
    print(os.getpid(), " - Starting")
    time.sleep(delay)
    subfunc()
    my_subprocess3.run_worker()
    print(os.getpid(), " - Continuing...")

def subfunc():
    process_logger.log("{} - processing....".format(os.getpid()))

if __name__ == "__main__":
    run_worker(0)
    # x = MySubprocess()
    # x.run(1)
