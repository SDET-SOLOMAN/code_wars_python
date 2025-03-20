# We are given two arrays of integers A and B and we have to output a sorted array with
# the integers that fulfill the following constraints:
#
# they are present in both ones
#
# they occur more than once in A and more than once in B
#
# their values are within a given range (inclusive)
#
# they are odd or even according as it is requested
#
# Example
# Given two arrays, a range, and a wanted parity:
#
# arrA = [1, -2, 7, 2, 1, 3, 7, 1, 0, 2, 3]
# arrB = [2, -1, 1, 1, 1, 1, 2, 3, 3, 7, 7, 0]
# rng = [-4, 4] # is the range of the integers from -4 to 4 (inclusive)
# wanted = "odd"
# Process to obtain the result:
#
# 0, 1, 2, 3, 7, are the numbers present in arrA and arrB
# 1, 2, 3, 7,  occur twice or more in arrA and arrB
# 1, 2, 3,  are in the range [-4, 4]
# 1, 3, are odd
# output = [1, 3]
# For the case:
#
# arrA = [1, -2, 7, 2, 1, 3, 4, 7, 1, 0, 2, 3, 0, 4]
# arrB = [0, 4, 2, -1, 1, 1, 1, 1, 2, 3, 3, 7, 7, 0, 4]
# rng = [-4, 4]
# wanted = "even"
# output = [0, 2, 4]
# If there are no elements that fulfill the constraints given above, the result will be an empty array.
#
# Features of the tests:
#
# Number of Random Tests = 300
# Length of the arrays A and B between 1000 and 10000
# You may assume that you will always receive valid entries for all the tests.
#
# Enjoy it!!

def find_arr(arr_a, arr_b, rng, wanted):
    print(rng)
    wanted = 0 if wanted == "even" else 1
    arr_a = sorted([x for x in arr_a if arr_a.count(x) > 1 and x % 2 == wanted])
    arr_b = sorted([x for x in arr_b if arr_b.count(x) > 1 and x % 2 == wanted])
    s = [x for x in arr_a if x in arr_b]
    final = sorted(set(s), key=lambda x: s.count(x), reverse=True)
    return [x for x in final if rng[0] <= x <= rng[1]]


def find_arr2(arr_a, arr_b, rng, wanted):
    # Convert parity string to number
    wanted_parity = 0 if wanted == "even" else 1

    # Build frequency dictionaries manually
    freq_a = {}
    freq_b = {}

    # Count occurrences in arr_a
    for num in arr_a:
        freq_a[num] = freq_a.get(num, 0) + 1

    # Count occurrences in arr_b
    for num in arr_b:
        freq_b[num] = freq_b.get(num, 0) + 1

    # Find numbers satisfying all conditions
    result = []

    for num in freq_a:
        if (
                freq_a[num] > 1 and  # Appears more than once in arr_a
                freq_b.get(num, 0) > 1 and  # Appears more than once in arr_b
                rng[0] <= num <= rng[1] and  # Within the given range
                num % 2 == wanted_parity  # Matches the requested parity
        ):
            result.append(num)

    return sorted(result)
