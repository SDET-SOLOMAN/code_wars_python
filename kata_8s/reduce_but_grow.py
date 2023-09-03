# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

from functools import reduce


def grow(arr):
    my_num = 1
    for num in arr:
        my_num *= num
    return my_num


def grow2(arr):
    try:
        return reduce(lambda x, y: x * y, arr)
    except ZeroDivisionError as Zero:
        return None


from functools import reduce


def grow3(arr):
    return reduce(lambda x, y: x * y, sorted(arr))
