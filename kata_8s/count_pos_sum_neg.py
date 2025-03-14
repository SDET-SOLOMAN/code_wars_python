# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of
# negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
#
# Example
#
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    if not arr:
        return []

    p = []
    n = []
    [p.append(ne) if ne > 0 else n.append(ne) for ne in arr]

    return [len(p), sum(n)]


positives = lambda x: len(list(filter(lambda s: s > 0, x)))
negatives = lambda x: sum(map(lambda s: s if s < 0 else 0, x))

def count_positives_sum_negatives2(arr):
    return [positives(arr), negatives(arr)] if arr else []