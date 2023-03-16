# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside
# and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).

# Hint for R users:

# The length of string is not always the same as the number of characters
# For example: (Input1, Input2) --> output

# ("1", "22") --> "1221"
# ("22", "1") --> "1221"

def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a


def solution2(a, b):
    first = sorted([a, b], key=len, reverse=True)[0]
    second = sorted([a, b], key=len, reverse=True)[1]

    return second + first + second

