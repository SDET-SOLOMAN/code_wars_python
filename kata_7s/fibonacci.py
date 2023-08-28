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


def fibonacci2(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    my_list = [0, 1, 1]
    a = 1
    b = 1
    for n in range(2, n + 1):
        c = a
        a = b + a
        b = c
        my_list.append(a)
    return my_list[n]


# recurssion

def fibonacci7(n: int) -> int:
    if n <= 2:
        if n < 1:
            return 0
        else:
            return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
