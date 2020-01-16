from __future__ import print_function
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__
import os
import time
import random

class MySubprocess2():
    def __init__(self, process_logger=None):
        global print
        print = process_logger.print if process_logger != None else __builtin__.print

    def run_worker(self, delay):
        run_worker(delay)

def run_worker(delay):
    print(os.getpid(), " - Continued...")
    time.sleep(random.randint(0,1))
    print(os.getpid(), " - delay * 2 is ", delay*2)
    print(os.getpid(), " - Finished")
    print("--------------------------------------------------------")

if __name__ == "__main__":
    run_worker(0)