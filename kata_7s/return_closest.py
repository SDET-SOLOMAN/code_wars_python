# Given a number return the closest number to it that is divisible by 10.
#
# Example input:
#
# 22
# 25
# 37
# Expected output:
#
# 20
# 30
# 40

closest_multiple_10 = lambda num: (num // 10) * 10 if num % 10 < 5 else (num // 10 + 1) * 10


def closest_multiple_10_v1(i):
    if i % 10 < 5:
        return (i // 10) * 10
    return (i // 10 + 1) * 10


def closest_multiple_10_v2(i):
    return (i // 10) * 10 if i % 10 < 5 else (i // 10 + 1) * 10


def closest_multiple_10_v3(i):
    return (round(i, -1))
