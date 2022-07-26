import time
import threading


def calculate_sum_squares(n):
    sum_squares = 0 
    for i in range(n):
        sum_squares += i ** 2

    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()
    current_threads = []
    for i in range(5):
        maximum_value = (i+1)* 1000000
        t = threading.Thread(target = calculate_sum_squares, args = (maximum_value, ))
        t.start()
        current_threads.append(t)
        # calculate_sum_squares(maximum_value)
    
    for t in current_threads:
        t.join()
    
    print("calculating sum of squares took: ", round(time.time() - calc_start_time,1))


    sleep_start_time = time.time()
    current_threads = []
    for seconds in range(1,6):
        t = threading.Thread(target = sleep_a_little, args = (seconds, ))
        t.start()
        current_threads.append(t)
        # sleep_a_little(seconds)

    for t in current_threads:
        t.join()
    print("sleep took: ", round(time.time() - sleep_start_time,1))

if __name__ == "__main__":
    main()