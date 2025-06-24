import time
from multiprocessing import Pool, cpu_count

def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    # 创建进程池，进程数建议为cpu核心数
    with Pool(processes=cpu_count()) as pool:
        pool.map(cpu_bound,numbers)
    # calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()
