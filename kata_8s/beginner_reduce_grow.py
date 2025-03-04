# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product


from functools import reduce

def grow2(arr):
    return reduce(lambda x, y: x * y, arr)