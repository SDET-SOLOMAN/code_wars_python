# Task
#
# Given an array of positive integers a and an integer k, find the first and last index of
# the longest subarray of a that consists only of k.
#
# If the array contains multiple subarrays of the same length, return indices of the last one.
#
# If k doesn't exist in a, return (-1, -1).
#
# Input/Output
#
# [input] integer array a
# A non-empty array. For each valid i 1 ≤ a[i] ≤ 9.
#
# [input] integer k
# 1 ≤ k ≤ 9.
#
# [output] an integer array
# The first and the last indices of the longest subarray consisting of k only,
# as an array in the format (start, end), or (-1, -1) if k is not present in a.
#
# Example
#
# For a = [2,1,1,1,1,3,3,4,5,1,1,1] and k = 3,
#
# the output should be (5, 6).
#
# The longest subarray of a that contains 3s starts at index 5 and ends at index 6.
#
# For a = [2,1,1,1,1,3,3,4,5,1,1,1,1] and k = 1,
#
# the output should be (9, 12).
#
# There are two subarrays of 1, and they have equal length. One goes from index 1 to 4, and another one
# from index 9 to 12. The answer should be (9, 12) as it is the last to occur.
#
# For a = [1, 2, 3] and k = 9,
#
# the output should be (-1, -1).

def find_subarray_with_same_element(a, k):
    re = (0, 0)
    counter = 0

    temp = 0
    n = -1

    if k not in a:
        return -1, -1

    for i, char in enumerate(a):
        if char == k:
            temp += 1
            if n == -1:
                n = i
            if i == len(a) - 1 and temp >= counter:
                re = (n, i)
                counter = temp
        else:
            if temp >= counter:
                re = (n, i - 1)
                counter = temp
            temp = 0
            n = -1
    return re


def find_subarray_with_same_element2(array, key):
    if key not in array:
        return (-1, -1)
    start = 0
    end = 0
    longest = [0, 0]
    while start < len(array) - 1:
        end = start
        if array[start] == key:

            while end < len(array) and array[end] == key:
                end += 1
            end -= 1
            print(start, end)
            if end - start >= longest[1] - longest[0]:
                longest = [start, end]
        start = end + 1
    return (longest[0], longest[1])