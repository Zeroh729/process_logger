import os
import time
import my_subprocess3
import process_logger as pl

def initLogging(logfilename):
    pl.init(logfilename)

def run_worker(delay):
    pl.log("Starting my_subprocess 1 by", os.getpid())
    print("--------------------------------------------------------")
    pl.writeOutput("--------------------------------------------------------")

    print(os.getpid(), " - Starting")
    pl.writeOutput(os.getpid(), " - Starting")

    time.sleep(delay)

    subfunc()

    my_subprocess3.run_worker()

    print(os.getpid(), " - Continuing...")
    pl.log("Finised my_subprocess 1")

def subfunc():
    print(os.getpid(), " - processing....")
    pl.writeOutput(os.getpid(), " - processing....")

if __name__ == "__main__":
    run_worker(0)
