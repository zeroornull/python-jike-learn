import sys

a = []

# 两次引用，一次来自 a，一次来自 getrefcount
print(sys.getrefcount(a))


def func(a):
    # 四次引用，a，python 的函数调用栈，函数参数，和 getrefcount
    print(sys.getrefcount(a))


func(a)

# 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
print(sys.getrefcount(a))

# python 3.7
# 2
# 4
# 2

# python 3.13 变化了
# 函数参数引用优化：在 Python 3.13 里，解释器对函数参数的引用管理做了优化，去掉了之前多余的内部临时引用。
# 性能提升：这样做的主要目的是提升性能，减少不必要的引用计数操作，尤其是为了解决多线程和解释器锁方面的性能问题（PEP 703，Free-threaded Python 的推进）。
# 影响：这会导致 sys.getrefcount 在某些场景下比旧版本少 1。
# 2
# 3
# 2