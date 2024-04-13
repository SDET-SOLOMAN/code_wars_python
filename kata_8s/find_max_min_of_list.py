# Your task is to make two functions ( max and min, or maximum and minimum, etc.,
# depending on the language ) that receive a list of integers as input, and return
# the largest and lowest number in that list, respectively.
#
# Examples (Input -> Output)
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5


minimum = lambda x: sorted(x)[0]
maximum = lambda x: max(x)


def minimum(arr):
    my_num = arr[0]
    for num in arr:
        if num < my_num:
            my_num = num
    return my_num

def maximum(arr):
    my_num = arr[0]
    for num in arr:
        if num > my_num:
            my_num = num
    return my_num

def minimum2(arr):
    return sorted(arr)[0]
def maximum2(arr):
    return sorted(arr)[-1]