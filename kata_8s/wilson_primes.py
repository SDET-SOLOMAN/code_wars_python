# DESCRIPTION:
#
# Wilson primes satisfy the following condition. Let P represent a prime number.
#
# Then,
#
# ((P-1)! + 1) / (P * P)
# should give a whole number.
#
# Your task is to create a function that returns true if the given number is a Wilson prime.

def am_i_wilson(n):
    return True if n == 5 or n == 13 or n == 563 else False
    # or just return if n in [5, 13, 563]

