# Task
# Given an array arr and a number n. Call a pair of numbers from the array a Perfect Pair if their sum is equal to n.
#
# Find all of the perfect pairs and return the sum of their indices.
#
# Note that any element of the array can only be counted in one Perfect Pair. Also if there are multiple correct
# answers, return the smallest one.
#
# Example
# For arr = [1, 4, 2, 3, 0, 5] and n = 7, the result should be 11.
#
# Since the Perfect Pairs are (4, 3) and (2, 5) with indices 1 + 3 + 2 + 5 = 11.
#
# For arr = [1, 3, 2, 4] and n = 4, the result should be 1.
#
# Since the element at index 0 (i.e. 1) and the element at index 1 (i.e. 3) form the only Perfect Pair.
#
# Input/Output
# [input] integer array arr
# array of non-negative integers.
#
# [input] integer n
# positive integer
#
# [output] integer
# sum of indices and 0 if no Perfect Pair exists.

def pairwise(arr, n):
    counting_sums = []

    for num in range(len(arr) - 1):

        for num2 in range(num + 1, len(arr)):

            if num2 in counting_sums or num in counting_sums: continue

            if arr[num] + arr[num2] == n:
                counting_sums.append(num)
                counting_sums.append(num2)

    return sum(counting_sums)


def pairwise2(arr, n):
    c = []

    for i, char in enumerate(arr[:-1]):
        for j, char2 in enumerate(arr[i + 1:], start=i + 1):
            if i in c or j in c:
                continue
            if char + char2 == n:
                c.append(i)
                c.append(j)
    return sum(c)