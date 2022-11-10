# N:
#
# An array is called zero-plentiful if it contains multiple zeros, and every sequence of zeros is at least 4 items long.
#
# Your task is to return the number of zero sequences if the given array is zero-plentiful, oherwise 0.
#
# Examples
#
# [0, 0, 0, 0, 0, 1]  -->  1
# # 1 group of 5 zeros (>= 4), thus the result is 1
#
# [0, 0, 0, 0, 1, 0, 0, 0, 0]  -->  2
# # 2 group of 4 zeros (>= 4), thus the result is 2
#
# [0, 0, 0, 0, 1, 0]  -->  0
# # 1 group of 4 zeros and 1 group of 1 zero (< 4)
# # _every_ sequence of zeros must be at least 4 long, thus the result is 0
#
# [0, 0, 0, 1, 0, 0]  -->  0
# # 1 group of 3 zeros (< 4) and 1 group of 2 zeros (< 4)
#
# [1, 2, 3, 4, 5]  -->  0
# # no zeros
#
# []  -->  0
# # no zeros

def zero_plentiful(arr):
    zero_counter = 0
    zero_seq = 0
    if arr == []:
        return 0
    if len(arr) < 4:
        return 0
    index = 0
    while index < len(arr):
        while index < len(arr) and arr[index] == 0:
            zero_counter += 1
            index += 1
        if zero_counter >= 4:
            zero_seq += 1
            zero_counter = 0
            index += 1
        else:
            if zero_counter > 0:
                zero_seq -= 1
                zero_counter = 0
                index += 1
            index += 1
    if zero_seq < 1:
        return 0
    return zero_seq