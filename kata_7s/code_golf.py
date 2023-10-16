# Task:
# In this Golfing Kata, you are going to receive 2 non-negative numbers a and b, b is equal to or greater than a.
#
# Then do the following procedure:
#
# Add a to b, then divide it by 2 with integer division.
#
# Repeat the procedure until b is equal to a.
#
# Return how many times it took to make b equal to a.
#
# Now golf your code, the length limit is 35, in one line.
#
# (The length of reference solution is 31)
#
# Examples:
# a = 3 and b = 9
#
# b = (3 + 9) // 2 = 6  ---  1 time
#
# b = (3 + 6) // 2 = 4  ---  2 times
#
# b = (3 + 4) // 2 = 3  ---  3 times
#
# So the result for a=3 and b=9 is `3`.
# More examples:
#
# input --> output
#
# f(0, 0) --> 0
# f(1, 2) --> 1
# f(3, 9) --> 3
# f(4, 20) --> 5
# f(5, 36) --> 5

def f(a, b):
    n = 0
    while a != b:
        b = (a + b) // 2
        n += 1
    return n


f2 = lambda a, b: (b - a).bit_length()
