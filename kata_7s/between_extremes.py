# Given an array of numbers, return the difference between the largest and smallest values.
#
# For example:
#
# [23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).
#
# [1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1).
#
# The array will contain a minimum of two elements. Input data range guarantees that max-min
# will cause no integer overflow.

def between_extremes(n):
    if not n or len(n) < 2:
        return 0
    n = sorted(n)
    return n[-1] - n[0]


def between_extremes2(numbers):
    num = numbers[0]
    if all(x == num for x in numbers):
        return 0
    a = max([x for x in numbers])
    b = min([x for x in numbers])
    return abs(a - b)


def between_extremes3(numbers):
    mi = numbers[0]
    ma = numbers[0]

    for char in numbers:
        if char < mi:
            mi = char
        if char > ma:
            ma = char
    return ma - mi
