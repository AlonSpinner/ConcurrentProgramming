from multiprocessing import Pool, cpu_count
import time

def check_number_of_values_in_range(comp_list,lower,upper):
    number_of_hits = 0
    for i in range(lower,upper):
        if i in comp_list:
            number_of_hits += 1
    return number_of_hits

num_processes = 4
comparison_list = [1,2,3]
power_list = [3,4,5]

lower_and_upper_bounds = [(0, 25*10**6), (25*10**6, 50*10**6), (50*10**6, 75*10**6), (75*10**6, 100*10**6)]


prepared_list = []
for i in range(len(lower_and_upper_bounds)):
    prepared_list.append((comparison_list, *lower_and_upper_bounds[i]))

start_time = time.time()

num_cpu_available = cpu_count()
print('num_cpu_to_use', num_cpu_available)

with Pool(num_cpu_available - 1) as mp_pool:
    result = mp_pool.starmap(check_number_of_values_in_range, prepared_list)

# print(result)

print("Everything took", time.time() - start_time, 'seconds')