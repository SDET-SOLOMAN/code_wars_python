# You are given three integer inputs: length, minimum, and maximum.
#
# Return a string that:
#
# Starts at minimum
# Ascends one at a time until reaching the maximum, then
# Descends one at a time until reaching the minimum
# repeat until the string is the appropriate length
# Examples:
#
#  length: 5, minimum: 1, maximum: 3   ==>  "12321"
#  length: 14, minimum: 0, maximum: 2  ==>  "01210121012101"
#  length: 11, minimum: 5, maximum: 9  ==>  "56789876567"
# Notes:
#
# length will always be non-negative
# negative numbers can appear for minimum and maximum values
# hyphens/dashes ("-") for negative numbers do count towards the length
# the resulting string must be truncated to the exact length provided
# return an empty string if maximum < minimum or length == 0
# minimum and maximum can equal one another and result in a single number repeated for the length of the string

def ascend_descend(length, minimum, maximum):
    new_s = ''
    i = 0
    while i < length:
        for num in range(minimum, maximum + 1):
            new_s += str(num)
            i += 1
        for num in range(maximum - 1, minimum, -1):
            new_s += str(num)
            i += 1
    return new_s[:length]


def ascend_descend2(l, mini, maxi):
    new_s = ''

    if mini > maxi:
        return ''

    for char in range(0, l):
        new_s += ''.join(str(x) for x in range(mini, maxi + 1))
        new_s += ''.join(str(x) for x in range(maxi - 1, mini, -1))
    return new_s[:l]


def ascend_descend3(length, minimum, maximum):
    n = []
    for char in range(length):
        n.extend([x for x in range(minimum, maximum + 1)])
        n.extend([x for x in range(maximum - 1, minimum, -1)])
    return ''.join(str(x) for x in n[:length])[:length]