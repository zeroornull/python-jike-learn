def is_subsequence(a,b):
    b = iter(b)
    return all(i in b for i in a)

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

print("================================================")

def is_subsequence_detail(a,b):
    b = iter(b)
    print(b)

    gen = (i for i in a)
    print(gen)

    for i in gen:
        print(i)

    gen = ((i in b) for i in a)
    print(gen)

    for i in gen:
        print(i)

    return all(((i in b) for i in a))

print(is_subsequence_detail([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence_detail([1, 4, 3], [1, 2, 3, 4, 5]))