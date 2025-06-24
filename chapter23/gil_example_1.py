from threading import Thread
import time


def CountDown(n):
    while n> 0:
        n -=1

n = 100000000

start_time = time.perf_counter()
# CountDown(n)
t1 = Thread(target=CountDown, args=[n//2])
t2 = Thread(target=CountDown, args=[n//2])
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.perf_counter()
print('Calculation takes {} seconds'.format(end_time - start_time))
