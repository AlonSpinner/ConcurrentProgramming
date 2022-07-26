import time
import threading

from workers.SleepyWorkers import SleepyWorker
from workers.SquaredSumWorkers import SquaredSumWorker

def main():
    calc_start_time = time.time()
    current_workers = []
    for i in range(5):
        maximum_value = (i+1)* 1000000
        ssw = SquaredSumWorker(n = maximum_value, daemon = True)
        current_workers.append(ssw)
    
    for w in current_workers:
        w.join()
    
    print("calculating sum of squares took: ", round(time.time() - calc_start_time,1))


    sleep_start_time = time.time()
    current_workers = []
    for seconds in range(1,6):
        slpyw = SleepyWorker(seconds = seconds, daemon = True)
        current_workers.append(slpyw)

    # for w in current_workers:
    #     w.join()
    print("sleep took: ", round(time.time() - sleep_start_time,1))

if __name__ == "__main__":
    main()