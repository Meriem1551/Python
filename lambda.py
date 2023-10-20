nums = [1, 2, 3, 4, 5, 6]


def square(num):
    return num * num


print(list(map(lambda n: n * n, nums)))

print(list(map(square, nums)))
