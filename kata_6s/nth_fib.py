# I love Fibonacci numbers in general, but I must admit I love some more than others.
#
# I would like for you to write me a function that, when given a number n (n >= 1 ), returns the nth number in the
# Fibonacci Sequence.
#
# For example:
#
#    nth_fib(4) == 2
# Because 2 is the 4th number in the Fibonacci Sequence.
#
# For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum
# of the previous two.

def nth_fib(n):
    if n == 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return 1
    m = [0, 1, 1, 2]

    for num in range(4, n):
        m.append(m[-1] + m[-2])
    return m[-1]


def nth_fib2(n):
    if not n:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    n1 = 1
    n2 = 1
    for char in range(2, n - 1):
        n3 = n1
        n1 = n2 + n1
        n2 = n3
    return n1


def nth_fib3(n):
    a = 0
    b = 1

    for char in range(0, n - 1):
        a, b = b, a + b

    return a