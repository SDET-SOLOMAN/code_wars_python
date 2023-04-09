from functools import reduce

a = [1, 2, 3]

print(reduce(lambda x, y: x * y, a, 5))
