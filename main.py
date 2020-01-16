from __future__ import print_function
import multiprocessing
import signal
import random
import datetime as dt

import my_subprocess
import my_subprocess2
import logging
from common import *
import process_logger as pl


def call_subprocess(params):
    mylogger = pl.ProcessLogger(loggerfilename)
    print = mylogger.print
    print("Params are ", params)

    mySubprocess = my_subprocess.MySubprocess(mylogger)
    mySubprocess2 = my_subprocess2.MySubprocess2(mylogger)
    mySubprocess.run_worker(params)
    mySubprocess2.run_worker(params)

    mylogger.printToMain()

def initLogging():
    global loggerfilename
    loggerfilename = "log/jsa_run_" + dt.datetime.now().strftime("%y%m%d_%H%M%S") + ".log"

def main():
    initLogging()
    print = pl.ProcessLogger(loggerfilename, isMainProcess = True).print
    print("Initializing 4 workers", isLogOnly=True)

    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    pool = multiprocessing.Pool(4)
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        print("Starting 10 jobs of 0-5 seconds each")
        # res = pool.map_async(call_subprocess, [random.randint(0,5) for i in range(10)])
        res = [pool.apply_async(call_subprocess, (random.randint(0,5),)) for i in range(10)]
        print("Waiting for results")
        for r in res:
            r.get(60) # Without the timeout this blocking call ignores all signals.
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
    else:
        print("Normal termination")
        pool.close()
    pool.join()

if __name__ == "__main__":
    main()