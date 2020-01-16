from __future__ import print_function
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__
import os
import time
import my_subprocess3

class MySubprocess():
    def __init__(self, process_logger=None):
        global print
        print = process_logger.print if process_logger != None else __builtin__.print
        self.sub = my_subprocess3.MySubprocess3(process_logger)

    def run_worker(self, delay):
        run_worker(delay, self.sub)

def run_worker(delay, sub=my_subprocess3.MySubprocess3()):
    print("--------------------------------------------------------")
    print(os.getpid(), " - Starting")
    time.sleep(delay)
    subfunc()
    sub.run_worker()
    print(os.getpid(), " - Continuing...")

def subfunc():
    print(os.getpid(), " - processing....")

if __name__ == "__main__":
    run_worker(0)
    # x = MySubprocess()
    # x.run(1)
