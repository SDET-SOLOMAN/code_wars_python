# You will be given an array and a limit value. You must check that all values in the array are below
# or equal to the limit value. If they are, return true. Else, return false.
#
# You can assume all values in the array are numbers.


def small_enough(array, limit):
    return len(list(filter(lambda x: x <= limit, array))) == len(array)


# using ALL

def small_enough2(array, limit):
    return all([x <= limit for x in array])