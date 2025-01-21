# Description:
# If you can't sleep, just count sheeps!!
#
# Task:
# Given a non-negative integer, 3 for example, return a string with a
# murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid,
# i.e. no negative integers.

def count_sheep(n):
    if not n:
        return ""
    return ''.join(f"{x} sheep..." for x in range (1, n + 1))


count_sheep2 = lambda n: ''.join(f"{x} sheep..." for x in range (1, n + 1))