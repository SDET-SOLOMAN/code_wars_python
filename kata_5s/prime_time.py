# We need prime numbers and we need them now!

# Write a method that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example,

# 11 => [2, 3, 5, 7, 11]

from typing import List


def is_prime(x: int) -> bool:
    if x < 2: return False
    if x % 2 == 0: return x == 2
    d, r = 3, int(x**0.5) + 1
    while d <= r:
        if x % d == 0: return False
def prime(n: int) -> List[int]:
    return [x for x in range(2, n + 1) if is_prime(x)]

