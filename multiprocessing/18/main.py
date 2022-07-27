from multiprocessing import Pool, cpu_count
from functools import partial
import time

def square(y, x):
    return x ** y

num_processes = 4
comparison_list = range(0,10000000)
power = 3

start_time = time.time()

num_cpu_available = cpu_count()
print('num_cpu_to_use', num_cpu_available)

partial_function = partial(square, power)

with Pool(num_cpu_available - 1) as mp_pool:
    result = mp_pool.map(partial_function, comparison_list)

# print(result)

print("Everything took", time.time() - start_time, 'seconds')