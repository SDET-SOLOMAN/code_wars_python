# Create function fib that returns n'th element of Fibonacci sequence (classic programming task).

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    n1 = 1
    n2 = 1

    for char in range(2, n):
        n1, n2 = n2, n1 + n2
    return n2