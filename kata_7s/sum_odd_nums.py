# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
#
# 1 -->  1
# 2 --> 3 + 5 = 8


def row_sum_odd_numbers(n):
    indexx = 0
    nn = n * (n - 1) + 1
    my_sum = 0
    while n > indexx:
        my_sum += nn
        nn = nn + 2
        indexx += 1
    return my_sum


# or super short one:
row_sum_odd_numbers2 = lambda n: n ** 3
