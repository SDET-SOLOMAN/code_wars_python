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


def zero_plentiful2(arr):
    zero_count = 0
    yes = 0
    index = 0
    print(arr)
    for char in arr:

        if char == 0:

            zero_count += 1

            if zero_count == 4:
                yes += 1

            if zero_count < 4 and index == len(arr) - 1:
                return 0

        elif char != 0:

            if zero_count >= 1 and zero_count < 4:
                return 0
            elif zero_count >= 4:
                zero_count = 0
        index += 1
    return yes


def zero_plentiful3(arr):

    zc = 0
    t = 0

    for i, c in enumerate(arr):

        if c == 0:
            zc += 1

            if i == (len(arr) - 1) and zc >= 4:
                t += 1
                return t

            elif i == len(arr) - 1 and zc:
                return 0

        else:
            if zc > 3:
                t += 1
                zc = 0
            if zc > 0:
                return 0
    return t

def zero_plentiful4(arr):
    z = 0
    total = 0

    for num in arr + [None]:  # Adding a sentinel value to process the final sequence
        if num == 0:
            z += 1
        else:
            if z and z < 4:  # Invalid sequence of zeros
                return 0
            if z >= 4:  # Valid sequence of zeros
                total += 1
            z = 0  # Reset count for the next sequence

    return total