# Task Overview
#
# Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.


# to_binary(1)  # should return 1
# to_binary(5)  # should return 101
# to_binary(11) # should return 1011

def bin_maker(num):
    str_num = ''
    while num > 0:
        str_num += str(num % 2)
        num //= 2
    return str_num[::-1]


def to_binary(n):
    return int(bin_maker(n))


# ------------

def to_binary2(n):
    return int(bin(n)[2:])