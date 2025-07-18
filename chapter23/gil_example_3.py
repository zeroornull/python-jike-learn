import threading

n = 0
lock = threading.Lock()


def foo():
    global n
    with lock:
        n += 1


threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)
