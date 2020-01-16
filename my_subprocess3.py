from __future__ import print_function
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__
import os
import time

class MySubprocess3():
    def __init__(self, process_logger=None):
        global print
        print = process_logger.print if process_logger != None else __builtin__.print

    def run_worker(self):
        run_worker()

def run_worker():
    print(os.getpid(), " - Beep boob.")
    subfunc()

def subfunc():
    print(os.getpid(), " - I was called by another module!")

if __name__ == "__main__":
    run_worker()