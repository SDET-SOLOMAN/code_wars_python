# In this Kata, you will be given two numbers, a and b, and your task is to determine if the first number
# a is divisible by all the prime factors of the second number b. For example: solve(15,12) = False because
# 15 is not divisible by all the prime factors of 12 (which include2).
#
# See test cases for more examples.

def solve(a,b):
    return a**10 % b == 0



def solve(a, b):
    p = 2
    while b > 1:
        while b % p:
            p += 1
        b //= p
        if a % p:
            return False
    return True