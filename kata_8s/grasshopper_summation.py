# Summation
# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
#
# For example (Input -> Output):
#
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

from functools import reduce

summation = lambda n: reduce(lambda x,y: x + y, range(1, n + 1))


def summation2(num):
    return sum(n for n in range(1, num + 1))
