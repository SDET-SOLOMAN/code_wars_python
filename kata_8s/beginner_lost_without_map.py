# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]

def maps(a):
    return [x * 2 for x in a]


def maps2(a):
    return list(map(lambda x: x * 2, a))


def maps3(a):
    return map(lambda x:2*x, a)


# using function within function

multi = lambda x: x * 2

def maps4(a):
    return list(map(multi, a))
