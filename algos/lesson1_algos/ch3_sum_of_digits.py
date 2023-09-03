# generate a sum of 3 digits and sum of any digit inputs
import math

# 1 convert to str and use for loop

# 2 using Modulo %
# randint(101, 999)
# first_num = num % 10
# remainder_num = num // 10
# second_num = remainder_num % 10
# third num = remainder_num // 10

import functools

a = 567423

print(sum(int(x) for x in str(a)))
print(functools.reduce(lambda x, y: x + y, [int(x) for x in str(a)]))
