# Task:
#
# Your job here is to write a function (keepOrder in JS/CoffeeScript,
# keep_order in Ruby/Crystal/Python, keeporder in Julia), which takes a sorted array ary and a value val,
# and returns the lowest index where you could insert val to maintain the sorted-ness of the array.
# The input array will always be sorted in ascending order. It may contain duplicates.
#
# Do not modify the input.
#
# Some examples:
#
# keep_order([1, 2, 3, 4, 7], 5) #=> 4
#                       ^(index 4)
# keep_order([1, 2, 3, 4, 7], 0) #=> 0
#           ^(index 0)
# keep_order([1, 1, 2, 2, 2], 2) #=> 2
#                 ^(index 2)


def keep_order(ary, val):
    for i, c in enumerate(ary):
        if val <= c:
            return i
    return len(ary)


def keep_orde2r(ary, val):
    a = [ary.index(x) for x in ary if val <= x]
    if not a:
        return len(ary)
    return a[0]