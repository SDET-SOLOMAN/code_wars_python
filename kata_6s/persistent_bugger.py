# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.
#
# For example (Input --> Output):
#
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)


def persistence(n):
    counter = 0
    if n  < 10:
        return 0
    while n >= 10:
        nums = 1
        for num in str(n):
            nums *= int(num)
        n = nums
        counter += 1
    return counter

# not converting to string, using modulo

def persistence2(n):
    c = 0
    while n > 9:
        m = 1
        s = n
        while s > 0:
            m *= s % 10
            s //= 10
        c += 1
        n = m
    return c