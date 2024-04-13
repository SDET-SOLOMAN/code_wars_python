# Complete the square sum function so that it squares each number passed into it
# and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because
# 1
# 2
# +
# 2
# 2
# +
# 2
# 2
# =
# 9
# 1
# 2
#  +2
# 2
#  +2
# 2
#  =9.

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


from functools import reduce as R


def square_sum2(numbers):
    return R(lambda x, y: x + y, (n ** 2 for n in numbers)) if numbers else 0
