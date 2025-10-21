# Given an array containing only zeros and ones, find the index of the zero that, if converted to one, will make the longest sequence of ones.
#
# For instance, given the array:
#
# [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
# replacing the zero at index 10 (counting from 0) forms a sequence of 9 ones:
#
# [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]
#                   '------------^------------'
# Your task is to complete the function that determines where to replace a zero with a one to make the maximum length subsequence.
#
# Notes:
#
# If there are multiple results, return the last one:
# [1, 1, 0, 1, 1, 0, 1, 1] ==> 5
#
# The array will always contain only zeros and ones.
# Can you do this in one pass?

def replace_zero(a):
    left = 0
    zero_idx = -1
    best_len = 0
    best_zero = -1

    for right, v in enumerate(a):

        if v == 0:
            left = zero_idx + 1
            zero_idx = right

        win_len = right - left + 1
        if win_len >= best_len:
            best_len = win_len
            best_zero = zero_idx

    return best_zero