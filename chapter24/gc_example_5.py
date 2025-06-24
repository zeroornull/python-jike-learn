import sys

a = []

# 两次引用，一次来自 a，一次来自 getrefcount
print(sys.getrefcount(a))

b = a

# 三次
print(sys.getrefcount(a))

c = b
d = b
e = c
f = e
g = d

# 八次
print(sys.getrefcount(a))
