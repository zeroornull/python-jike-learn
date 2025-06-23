import os
import time

import psutil

# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    # 加.的目的时表示浮点数而不是整数
    memory = info.uss /1024./1024
    print('{} memory used: {} MB'.format(hint, memory))

def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')

def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')

start = time.time()
test_iterator()
print("test_iterator time:", time.time() - start, "seconds")

start = time.time()
test_generator()
print("test_generator time:", time.time() - start, "seconds")