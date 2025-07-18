import cProfile


def memorize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memorize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n - 1))
    res.append(fib(n))
    return res


# fib_seq(30)
cProfile.run('fib_seq(30)')
