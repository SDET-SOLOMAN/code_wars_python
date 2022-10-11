# factorial recursion
from python_challenges.day2.day2_hw import dig_root


def factorial_rec(num):
    if num < 0:
        return "Only positive nums"
    if num == 0 or num == 1:
        return 1
    return num * factorial_rec(num - 1)


print(factorial_rec(4))


def digital_root_rec(num):
    if num < 10:
        return num
    return digital_root_rec(dig_root(num))


print(digital_root_rec(543210))


def fib_rec(num):
    if num < 0:
        return "Only positive nums"
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return fib_rec(num - 1) + fib_rec(num - 2)


print(fib_rec(4))