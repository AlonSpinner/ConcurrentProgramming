from multiprocessing import Pool, cpu_count
import time

def square(x):
    return x ** 2

num_processes = 4
comparison_list = range(0,10000000)


start_time = time.time()

num_cpu_available = cpu_count()
print('num_cpu_to_use', num_cpu_available)

with Pool(num_cpu_available - 1) as mp_pool:
    result = mp_pool.map(square, comparison_list)

# print(result)

print("Everything took", time.time() - start_time, 'seconds')