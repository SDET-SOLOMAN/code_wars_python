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
