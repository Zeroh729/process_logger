import os
import time
import random
import process_logger as pl

def initLogging(logfilename):
    pl.init(logfilename)

def run_worker(delay):
    print(os.getpid(), " - Continued...")
    time.sleep(random.randint(0,1))
    print(os.getpid(), " - delay * 2 is ", delay*2)
    print(os.getpid(), " - Finished")
    print("--------------------------------------------------------")

if __name__ == "__main__":
    run_worker(0)