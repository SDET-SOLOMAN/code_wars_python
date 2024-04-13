# DESCRIPTION:
#
# Given a string, your task is to count the number and length of arrow symbols in that string
# and return an int using the following rules:
#
# The string will only contain the characters ., -, =, <, >.
# An arrow must start with either < or >.
# Arrows are scored based on their length and direction, for example:
# (Left-facing arrows are scored as negative, while Right-facing arrows are positive)
# > is scored as 1
# -> is scored as 2
# < is scored as -1
# <- is scored as -2
# An arrow's tail (if it has one) must be entirely made up of either - or =. You cannot mix.
# So, --> would be a valid arrow of length 3, but =-> would only count -> as a part of the arrow.
# Additionally, arrows with a tail of = are scored twice as high as arrows with a tail of -, for example:
# --> is scored as 3
# ==> is scored as 6
# <= is scored as -4
# Double-sided arrows, like <-> or <===> are counted as 0.
# . is an empty character and cannot be the tail of an arrow.
# Examples
#
#     arrow_search('>.') # 1
#     arrow_search('<--..') # -3
#     arrow_search('><=><--') # -2
#     arrow_search('>===>->') # 11

def arrow_search(str) -> int:
    s = 0
    z = 0
    m = 0
    n = 0
    for a in str:
        if a == '.':
            if z < 0:
                s -= (1 if m == 0 else (n + 1)*m)
            z = m = n = 0
        elif a == '>':
            if z == 0:
                s += (1 if m == 0 else (n + 1)*m )
            z = m = n = 0
        elif a == '<':
            if z < 0:
                s -= (1 if m == 0 else (n + 1)*m)
            z = -1
            m = n = 0
        elif a == '-':
            if m < 2:
                n += 1
            elif m == 2 and z < 0:
                s -= (n + 1)*m
                z = 0
                n = 1
            else:
                n = 1
            m = 1
        elif a == '=':
            if m == 0 or m == 2:
                n += 1
            elif m == 1 and z < 0:
                s -= (n + 1)
                z = 0
                n = 1
            else:
                n = 1
            m = 2
    return (s - (1 if m == 0 else (n + 1)*m)) if  z < 0 else s