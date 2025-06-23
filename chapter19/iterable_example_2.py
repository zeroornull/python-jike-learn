def index_generator(L,target):
    for i , num in enumerate(L):
        if num == target:
            yield i

print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))