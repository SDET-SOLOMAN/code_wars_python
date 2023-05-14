from functools import reduce
import math as my_math

a = [1, 2, 3]

print(reduce(lambda x, y: x * y, a, 5))


lis_t = [1, 2, 3, 4, 5, 6]
print(reduce(lambda x, y: x*y, lis_t))
print(my_math.prod(lis_t))