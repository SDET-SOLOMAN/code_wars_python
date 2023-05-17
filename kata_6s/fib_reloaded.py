# And here is Fibonacci again. This time we want to go one step further. Our fib()
# function must be faster! Can you do it?
#
# In case you don't know, what the Fibonacci number is:
#
# The nth Fibonacci number is defined by the sum of the two previous Fibonacci numbers.
# In our case: fib(1) := 0 and fib(2) := 1. With these initial values you should be able
# to calculate each following Fibonacci number.
#
# Examples:
#
# fib(1) // === 0
# fib(2) // === 1
# fib(3) // === 1
# fib(4) // === 2
# fib(5) // === 3

def fib(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1

    my_fib = [0, 1, 1]

    for char in range(2, n - 1):
        my_fib.append(my_fib[-1] + my_fib[-2])
    return my_fib[-1]


def fib2(n):
    n1 = 0
    n2 = 1
    for char in range(1, n):
        n1, n2 = n2, n1 + n2
    return n1