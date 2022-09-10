# Introduction
import math

# The first century spans from the year 1 up to and including the year 100, the second century -
# from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples:
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

my_year = 1901


def century(year):
    # or return math.ceil(year / 100)
    # or return ((year) + 99) // 100
    return ((year - 1) // 100) + 1


print(century(my_year))
print(math.ceil(my_year / 100))
print((my_year + 99) // 100)
