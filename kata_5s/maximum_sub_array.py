# The maximum sum subarray problem consists in finding the maximum sum of a contiguous
# subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the
# sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarr

def max_sequence(arr):
    current = 0
    max_found = 0
    for v in arr:
        current += v
        if current <= 0:
            current = 0
        if current > max_found:
            max_found = current
    return max_found


def max_sequence2(arr):
    curr_max_sum = 0
    global_max = 0
    for i in arr:
        curr_max_sum = max(curr_max_sum + i, i)
        global_max = max(curr_max_sum, global_max)
        print(f"this is i {i}, this is curr max {curr_max_sum} and this is global max {global_max}")
    return global_max
