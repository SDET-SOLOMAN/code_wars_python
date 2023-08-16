# The Stanton measure of an array is computed as follows: count the number of occurences for value 1 in the array.
# Let this count be n. The Stanton measure is the number of times that n appears in the array.
#
# Write a function which takes an integer array and returns its Stanton measure.
#
# Examples
#
# The Stanton measure of [1, 4, 3, 2, 1, 2, 3, 2] is 3, because 1 occurs 2 times in the array and 2 occurs 3 times.
#
# The Stanton measure of [1, 4, 1, 2, 11, 2, 3, 1] is 1, because 1 occurs 3 times in the array and 3 occurs 1 time.

# easiest solution:
def stanton_measure(arr):
    nums = arr.count(1)
    return arr.count(nums)


# without count:

def stanton_measure2(arr):
    my_one_count = 0
    for char in arr:
        if char == 1:
            my_one_count += 1

    my_return_count = 0
    for char in arr:
        if char == my_one_count:
            my_return_count += 1

    return my_return_count


# using reduce

from functools import reduce


def stanton_measure3(arr):
    one = [1 for x in arr if x == 1]
    one_count = reduce(lambda x, y: x + y, one) if one else 0
    second = list(filter(lambda x: x == one_count, arr))
    return sum(1 for x in second if x == one_count)


def stanton_measure4(arr):
    first = len([1 for x in arr if x == 1])
    return len([1 for x in arr if x == first])


# one line
stanton_measure5 = lambda arr: len([1 for x in arr if x == len([1 for x in arr if x == 1])])


